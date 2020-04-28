from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    dob  = DateTimeField('Your Birthday', format='%m-%d-%y',validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class PostProductForm(FlaskForm):
    name = StringField('Title', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    quantity = StringField('Qty', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Length(min=1, max=400)])
    submit = SubmitField('Submit')

class UpdateProductForm(FlaskForm):
    name = StringField('Title', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    quantity = StringField('Qty', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Length(min=1, max=400)])
    submit = SubmitField('Update')