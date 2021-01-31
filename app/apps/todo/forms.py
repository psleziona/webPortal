from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField

class AddTask(FlaskForm):
    title = StringField('title')
    task = StringField('task')
    add = SubmitField('Add')
