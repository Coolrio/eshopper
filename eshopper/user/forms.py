from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from eshopper.user.modules import user_login


class RegistrationForm(FlaskForm):
    firstname = StringField('firstname',
                           validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField('lastname',
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    phonenumber = StringField('phonenumber',
                            validators=[DataRequired(), Length(min=10, max=13)])
    pincode = StringField('pincode',
                            validators=[DataRequired(), Length(min=6, max=6)])
    city = StringField('city',
                            validators=[DataRequired(), Length(min=2, max=20)])
    landmark = StringField('landmark',
                            validators=[DataRequired(), Length(min=2, max=20)])
    houseno = StringField('house Number',
                            validators=[DataRequired(), Length(min=2, max=20)])
    state = StringField('state',
                            validators=[DataRequired(), Length(min=2, max=20)])
    country = StringField('country',
                        validators=[DataRequired(), Length(min=2, max=20)])
    address = StringField('address',
                        validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_firstname(self, firstname):
        user = user_login.query.filter_by(firstname=firstname.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = user_login.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

