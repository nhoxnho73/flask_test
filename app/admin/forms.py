from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class DepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    # text box
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    # button
    submit = SubmitField('Submit')
