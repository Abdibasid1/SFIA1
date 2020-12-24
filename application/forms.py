from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired
from application.models import Club

class BoxerForm(FlaskForm):
    firstname = StringField('The boxers firstname', validators=[DataRequired()])
    lastname = StringField('The boxers lastname', validators=[DataRequired()])
    email = StringField('The boxers email', validators=[DataRequired()])
    weightclass = StringField('The weightclass', validators=[DataRequired()])
    club = SelectField(' Choose club', choices=[(c.id, c.clubname) for c in Club.query.order_by("clubname") ])
    submit = SubmitField('Add Boxer')

class ClubForm(FlaskForm):
    clubname = StringField('The club name', validators=[DataRequired()])
    clublocation = StringField('The club location', validators=[DataRequired()])
    email = StringField('The club email', validators=[DataRequired()])
    clubmanager = StringField('The manager', validators=[DataRequired()])
    submit = SubmitField('Add club')

