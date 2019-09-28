from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, Email, EqualTo

# RegistrationForm inheriting from FlaskForm
class RegistrationForm(FlaskForm):

    # Instantiating Field objects from wtforms

    # StringField represents <input type="text"> element
    username = StringField('Username', 
                            validators=[InputRequired(), Length(min = 2, max=20)])
    email = StringField('Email',
                            validators=[InputRequired(), Email()]) 
    password = PasswordField('Password',
                            validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password',
                            validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up') # Button

# LoginForm inheriting from FlaskForm
class LoginForm(FlaskForm):

    # Instantiating field objects from wtforms
    email = StringField('Email',
                            validators=[InputRequired(), Email()]) 
    password = PasswordField('Password',
                            validators=[InputRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')