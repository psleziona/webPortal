from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class AddTask(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    task = TextAreaField('task', validators=[DataRequired()])
    add = SubmitField('Add task')
