

from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Length

from app.models import User
from wtforms.validators import ValidationError,Email

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=10)])
    confirmpassword = PasswordField('Repeat Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')




    def validate_username(self, username):
        users = User.query.filter_by(username = username.data).first()
        if users is not None:
            raise ValidationError('Please use a different username')

    def validate_email(self, email):
        users= User.query.filter_by(email=email.data).first()
        if users is not None:
            raise ValidationError('Please use different email address')