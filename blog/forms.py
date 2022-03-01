from distutils.command.config import config
from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from blog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(),Length(min=2, max=20)])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(),Length(min=8)])
    confirm_password = PasswordField('confirm password', 
                                validators=[DataRequired(),Length(min=8), EqualTo('password')])
    submit = SubmitField('sign up')

    # validation
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is taken. Try another one')

    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first() #if there's a user, return the first. else, none.
        if user: #if user exist
            raise ValidationError('There is an account for this email already. Try another one') #validation error


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(),Length(min=8)])
    remember =  BooleanField('remember me')
    submit = SubmitField('login')