from flask import render_template, flash, redirect, url_for, request, abort
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm, RegistrationForm, PostProductForm, UpdateProductForm
from app.models import User, Product
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
@login_required
def index():
    products = Product.query.all()

    products +=  [
   {
       'seller': {'username': 'Josh'},
       'name': 'oven',
       'price': 200.51,
       'quantity': 6,
       'description': 'You can cook things with this'
   },
   {
       'seller': {'username': 'Amazon'},
       'name': 'Cutting Board',
       'price': 18.97,
       'quantity': 20,
       'description': 'Save your counter and cut food on this'
   },
   {
       'seller': {'username': 'Walmart'},
       'name': 'Nintendo Switch',
       'price': 300.00,
       'quantity': 1,
       'description': 'Play games on the go'
   },
   {
       'seller': {'username': 'Target'},
       'name': 'Mug',
       'price': 7.00,
       'quantity': 32,
       'description': 'keep your beverage warm with this mug'
   },
   {
       'seller': {'username': '7-Eleven'},
       'name': 'cheetos',
       'price': 1.00,
       'quantity': 50,
       'description': 'Snack'
   },
   {
       'seller': {'username': 'Circle K'},
       'name': 'cheetos',
       'price': 3.00,
       'quantity': 20,
       'description': 'Food'
   },
   {
       'seller': {'username': 'Home Depot'},
       'name': 'Paint',
       'price': 21.99,
       'quantity': 3,
       'description': 'Save your counter and cut food on this'
   },
   {
       'seller': {'username': 'Gamestop'},
       'name': 'Nintendo Switch',
       'price': 299.99,
       'quantity': 7,
       'description': 'play video games'
   },
   {
       'seller': {'username': 'Walmart'},
       'name': 'Nintendo Switch',
       'price': 300.00,
       'quantity': 1,
       'description': 'Save your counter and cut food on this'
   },
   {
       'seller': {'username': 'Walmart'},
       'name': 'Nintendo Switch',
       'price': 300.00,
       'quantity': 1,
       'description': 'Save your counter and cut food on this'
   },
   {
       'seller': {'username': 'Dollar General'},
       'name': 'Water',
       'price': 1.00,
       'quantity': 63,
       'description': 'Water'
   },
   {
       'seller': {'username': 'Dollar Tree'},
       'name': 'Water',
       'price': 2.00,
       'quantity': 62,
       'description': 'Water'
   },
   {
       'seller': {'username': 'Giant Eagle'},
       'name': 'Chicken',
       'price': 22.00,
       'quantity': 42,
       'description': 'Chicken'
   },
   {
       'seller': {'username': 'ALDI'},
       'name': 'Chicken',
       'price': 19.99,
       'quantity': 1,
       'description': 'Chicken'
   },
   {
       'seller': {'username': 'Sam'},
       'name': 'Mask',
       'price': 5.99,
       'quantity': 8,
       'description': 'Mask'
   },
   {
       'seller': {'username': 'May'},
       'name': 'Mask',
       'price': 4.99,
       'quantity': 2,
       'description': 'Mask'
   },
   {
       'seller': {'username': 'Costco'},
       'name': 'Milk',
       'price': 3.99,
       'quantity': 9,
       'description':'Milk'
   },
   {
       'seller': {'username': 'Rite Aid'},
       'name': 'Milk',
       'price': 7.99,
       'quantity': 99,
       'description': 'Milk'
   },
   {
       'seller': {'username': 'Best Buy'},
       'name': 'Monitor',
       'price': 212.63,
       'quantity': 100,
       'description': 'MSI Monitor'
   },
   {
       'seller': {'username': 'Micro Center'},
       'name': 'Monitor',
       'price': 209.62,
       'quantity': 10,
       'description': 'MSI Monitor'
   },
   {
       'seller': {'username': 'Newegg'},
       'name': 'Monitor',
       'price': 196.60,
       'quantity': 2,
       'description': 'MSI Monitor'
   },
   {
       'seller': {'username': 'Nike'},
       'name': 'Shoes',
       'price': 99.52,
       'quantity': 101,
       'description': 'Shoes'
   },
   {
       'seller': {'username': 'Finish Line'},
       'name': 'Shoes',
       'price': 50.52,
       'quantity': 60,
       'description': 'Shoes'
   },
   {
       'seller': {'username': 'Adidas'},
       'name': 'Shoes',
       'price': 60.51,
       'quantity': 20,
       'description': 'Shoes'
   },
   {
       'seller': {'username': 'Skechers'},
       'name': 'Shoes',
       'price': 20.00,
       'quantity': 98,
       'description': 'Shoes'
   },
   {
       'seller': {'username': 'Microsoft'},
       'name': 'Surface Pro X',
       'price': 899.99,
       'quantity': 2000,
       'description': '2-in-1 laptop'
   },
   {
       'seller': {'username': 'Microsoft'},
       'name': 'Surface Pro X',
       'price': 899.99,
       'quantity': 2000,
       'description': '2-in-1 Laptop'
   },
   {
       'seller': {'username': 'Apple'},
       'name': 'MacBook Air',
       'price': 999.99,
       'quantity': 200,
       'description': 'Laptop'
   },
   {
       'seller': {'username': 'Apple'},
       'name': 'iPhone SE',
       'price': 399.99,
       'quantity': 250,
       'description': 'Phone'
   },
   {
       'seller': {'username': 'Samsung'},
       'name': 'Galaxy S20',
       'price': 1199.99,
       'quantity': 260,
       'description': 'Phone'
   },
   {
       'seller': {'username': 'Google'},
       'name': 'Pixel 4',
       'price': 499.99,
       'quantity': 1000,
       'description': 'Phone'
   },
   {
       'seller': {'username': 'Starbucks'},
       'name': 'Coffee',
       'price': 4.99,
       'quantity': 1000,
       'description': 'Coffee'
   },
   {
       'seller': {'username': 'Tim Hortons'},
       'name': 'Coffee',
       'price': 3.99,
       'quantity': 10001,
       'description': 'Coffee'
   },
   {
       'seller': {'username': 'Scribbles Coffee Co'},
       'name': 'Coffee',
       'price': 4.00,
       'quantity': 13,
       'description': 'Coffee'
   },
   {
       'seller': {'username': 'Bent Tree Coffee'},
       'name': 'Coffee',
       'price': 3.00,
       'quantity': 132,
       'description': 'Coffee'
   },
   {
       'seller': {'username': 'Sam Ash'},
       'name': 'Guitar',
       'price': 200.00,
       'quantity': 10,
       'description': 'Guitar'
   },
   {
       'seller': {'username': 'Guitar Center'},
       'name': 'Guitar',
       'price': 300.00,
       'quantity': 13,
       'description': 'Guitar'
   },
   {
       'seller': {'username': 'Barnes & Noble'},
       'name': 'Harry Potter',
       'price': 2.00,
       'quantity': 13,
       'description': 'Book'
   },
   {
       'seller': {'username': 'Half Price Books'},
       'name': 'Harry Potter',
       'price': 5.00,
       'quantity': 16,
       'description': 'Book'
   },
   {
       'seller': {'username': 'American Eagle'},
       'name': 'Jeans',
       'price': 35.97,
       'quantity': 16,
       'description': 'Pants made of denim'
   },
   {
       'seller': {'username': 'American Eagle'},
       'name': 'Jeans',
       'price': 45.27,
       'quantity': 36,
       'description': 'Pants made of denim'
   },
   {
       'seller': {'username': 'American Eagle'},
       'name': 'Jeans',
       'price': 45.27,
       'quantity': 36,
       'description': 'Pants made of denim'
   },
   {
       'seller': {'username': 'Nordstrom'},
       'name': 'Jeans',
       'price': 55.27,
       'quantity': 78,
       'description': 'Pants made of denim'
   },
   {
       'seller': {'username': 'Nordstrom'},
       'name': 'Jeans',
       'price': 62.73,
       'quantity': 88,
       'description': 'Pants made of denim'
   },
   {
       'seller': {'username': 'Old Navy'},
       'name': 'Jeans',
       'price': 40.00,
       'quantity': 28,
       'description': 'Pants made of denim'
   },
   {
       'seller': {'username': 'Old Navy'},
       'name': 'Jeans',
       'price': 35.00,
       'quantity': 68,
       'description': 'Pants made of denim'
   },
   {
       'seller': {'username': 'Staples'},
       'name': 'Pens',
       'price': 6.49,
       'quantity': 63,
       'description': 'Gel Pens'
   },
   {
       'seller': {'username': 'Staples'},
       'name': 'Pens',
       'price': 6.49,
       'quantity': 23,
       'description': 'Fine Point Pens'
   },
   {
       'seller': {'username': 'OfficeMax'},
       'name': 'Ballpoint Pens',
       'price': 4.99,
       'quantity': 43,
       'description': 'Ballpoint Pens'
   },
   {
       'seller': {'username': 'OfficeMax'},
       'name': 'Medium Point Pens',
       'price': 14.49,
       'quantity': 43,
       'description': 'Medium Point Pens'
   }
]

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


@app.route('/dashboard/<int:product_id>/delete',methods=['POST'])
@login_required
def delete(product_id):
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        flash('Product Deleted!')
        return redirect(url_for('dashboard'))

@app.route('/edit/<int:product_id>',methods=['GET','POST'])
@login_required
def edit(product_id):
        product = Product.query.get_or_404(product_id)
        if product.seller != current_user:
            abort(403)

        form = UpdateProductForm()
        form.name.data = product.name
        form.price.data = product.price
        form.quantity.data = product.quantity
        form.description.data = product.description

        if form.validate_on_submit():
            product.name = request.form['name']
            product.price = request.form['price']
            product.quantity = request.form['quantity']
            product.description = request.form['description']
            db.session.commit()
            flash('Product Updated!')
            return redirect(url_for('dashboard'))
        
        
        return render_template('edit.html', title='Edit',form=form)
        
    