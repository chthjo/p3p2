from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, Form, SelectField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User
from app.models import Calendar

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
            'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please enter a different username.')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class requestWeek(FlaskForm):
    week  = IntegerField('Enter a week number to request off:', validators=[DataRequired()])
    submit = SubmitField('Submit Request')

    def validate_week(self, week):
        wcheck = Calendar.query.filter_by(week=week.data).first()
        if wcheck is not None:
            raise ValidationError('This week is already being requested by a user')
class checkWeek(FlaskForm):
    week  = IntegerField('Enter a week number to check availability:')
    user  = StringField('Enter a user to see request history')
    submit = SubmitField('Submit Request')

