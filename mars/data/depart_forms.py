from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class DepartForm(FlaskForm):
    team_leader = IntegerField('id лидера', validators=[DataRequired()])
    title = StringField('List of Departments', validators=[DataRequired()])
    chief = StringField('Chief', validators=[DataRequired()])
    members = StringField('Members', validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    submit = SubmitField('Применить')