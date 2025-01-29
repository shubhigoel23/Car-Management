from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired

class CarForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    tags = StringField('Tags', validators=[DataRequired()])
    images = FileField('Upload Images', validators=[DataRequired()])
    submit = SubmitField('Create Car')
