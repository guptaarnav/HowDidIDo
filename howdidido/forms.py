from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired

class TestInfoForm(FlaskForm):
    avg = DecimalField('avg', validators=[DataRequired()])
    std = DecimalField('std', validators=[DataRequired()])
    score = DecimalField('score', validators=[DataRequired()])
    submit = SubmitField()