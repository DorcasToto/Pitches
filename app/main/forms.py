from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
from ..models import User

class updateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself',validators = [Required()])
    submit = SubmitField('Submit')
