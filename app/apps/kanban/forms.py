from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired

class AddTask(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    task = StringField('task', validators=[DataRequired()])
    add = SubmitField('Add', validators=[DataRequired()])
