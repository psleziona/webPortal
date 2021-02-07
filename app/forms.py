from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import Users

class PostForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    post = TextAreaField('post', validators=[DataRequired()])
    category = SelectField('category', choices=[('main', 'Main'),('personal', 'Personal'),('development', 'Development')])
    submit = SubmitField('Dodaj')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat password', validators=[DataRequired(), EqualTo('password')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Use diffrent username!')

    def validate_email(self, email):
        mail = Users.query.filter_by(email=email.data).first()
        print(mail)
        if mail is not None:
            raise ValidationError('Use diffrent e-mail!')
    

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first()
        if user is None:
            raise ValidationError('User doesn\'t exist!')


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Send')