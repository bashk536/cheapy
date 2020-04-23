from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm, RegistrationForm, PostProductForm
from app.models import User, Product
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
@login_required
def index():
    products = Product.query.all()
    return render_template('index.html', title='Home', products=products)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html',  title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(firstName=form.firstName.data,lastName=form.lastName.data,\
             dob=form.dob.data,username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/delete',methods=['POST'])
@login_required
def delete():
    product = Product.query.filter_by(id=current_user.products.id).first()
    db.session.delete(product)
    db.session.commit()
    flash('Product Deleted!')
    return render_template('dashboard.html', product=product)

@app.route('/sell', methods=['GET', 'POST'])
@login_required
def sell():
    form = PostProductForm()
    if form.validate_on_submit():
        product = Product(name=form.name.data,price=form.price.data,\
            quantity=form.quantity.data,description=form.description.data,seller=current_user)
        db.session.add(product)
        db.session.commit()
        flash('Thousands of users can see your item now')
        return redirect(url_for('sell'))

    return render_template('sell.html', title='Sell',form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    products = Product.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', title='DashBoard', products=products)
    