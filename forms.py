from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DecimalField, TextAreaField, DateField
from flask_wtf.file import FileField, FileRequired, FileAllowed
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

# NewProperty Form (For posting new properties to rent)
class NewPropertyForm(FlaskForm):

    # Instantiating field objects from wtforms
    post_title = StringField('Title',
                            validators=[InputRequired(), Length(min = 4, max=25)])
    house_type = StringField('House Type',
                            validators=[InputRequired(), Length(min = 3, max=20)])
    city = StringField('City',
                            validators=[InputRequired(), Length(min = 3, max=20)])
    daily_price = DecimalField('Daily Price', places=2)
    description = TextAreaField('Post Description',
                            validators=[InputRequired(), Length(min = 0, max=250)]) 
    submit = SubmitField('Submit Post')