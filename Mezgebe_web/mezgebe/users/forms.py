from flask import current_app
from mezgebe.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user


class UserRegisterationForm(FlaskForm):
    """
       Class Define Form/Fields To Recieve User Data
       During a New User Registeration/Sign Up Process

       - Extends FlaskForm
    """
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired() ])
    user_name = StringField('Username',
                            validators=[DataRequired(), Length(min=5, max=10)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('New Password',validators=[DataRequired()])
    confirm_password = PasswordField('Retype Your Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit_button = SubmitField('Sign Up')

    def validate_user_name(self, user_name):
        """
          Prevent user name repication in account creation
        """
        user = User.query.filter_by(user_name=user_name.data).first()
        if user:
            raise ValidationError('User name already taken. Please user another user name')


    def validate_email(self, email):
        """
          Prevent Email relplication in account creation
        """
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email already taken. Please use another email')



class UserLoginForm(FlaskForm):
    """
       Class Define Form / Fields Necessary During
       User Login Process

       - Extends FlaskForm
    """
    email = StringField('Email address',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit_button = SubmitField('Login')



class PasswordResetForm(FlaskForm):
    """
       Class Defone Form / Fields Necessary During
       Password Reset Process by a User

       - Extends FlaskForm
    """
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit_button = SubmitField('Reset Password')

    def validate_email(self, email):
        """
          Prevent Email relplication in account creation
        """
        email = User.query.filter_by(email=email.data).first()
        if not email:
            raise ValidationError('Email does not exit. Please create a New Account.')



class PasswordChangeForm(FlaskForm):
    """
       Class Defone Form / Fields Necessary During
       Password Change Process by a User

       - Extends FlaskForm
    """
    password = PasswordField('New Password',validators=[DataRequired()])
    confirm_password = PasswordField('Retype New Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit_button = SubmitField('Change Password')
