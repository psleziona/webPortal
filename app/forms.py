from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User

class PostForm(FlaskForm):
    title = StringField('title')
    post = TextAreaField('post')
    category = SelectField('category', choices=[('main', 'Main'),('personal', 'Personal'),('development', 'Development')])
    submit = SubmitField('Dodaj')


class RegisterForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    password2 = PasswordField('Repeat password')
    email = StringField('Email')
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username).first()
        if user is not None:
            raise ValidationError('Use diffrent username!')

    def validate_email(self, username):
        email = User.query.filter_by(email=email).first()
        if email is not None:
            raise ValidationError('Use diffrent e-mail!')
    

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Login')


class CommentForm(FlaskForm):
    username = StringField('Username')
    comment = TextAreaField('Comment')
    submit = SubmitField('Send')