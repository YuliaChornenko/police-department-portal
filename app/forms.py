from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from wtforms import validators
from flask import flash

class LoginForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=20)])
    password = PasswordField('Password', [validators.Length(min=6, max=50)])


class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=20)])
    email = StringField('Email Address', [Email(message=('Not a valid email address!', )), DataRequired()])
    password = PasswordField('Password', [
        validators.InputRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    key = StringField('Key')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice (updated Jan 22, 2015)',
                              [DataRequired()])

class ApplicationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=60)])
    location = StringField('Location', )
    application = TextAreaField('Application')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice (updated Jan 22, 2015)',
                              [DataRequired()])