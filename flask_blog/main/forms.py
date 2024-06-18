from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, PasswordField, SubmitField, BooleanField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from flask_blog.models import Users
import phonenumbers
class PhoneNumberValidation(FlaskForm):
    phone = StringField('Phone',validators=[DataRequired(),
        Regexp(r'^\+?[1-9]\d{1,14}$', message="Invalid phone number format.")])
    submit = SubmitField('Submit')
    
    # def validate_phone(form, field):
    #     if len(field.data) >16:
    #         raise ValidationError('Invalid Phone Number')
    #     try:
    #         input_number = phonenumbers.parse(field.data)
    #         if not (phonenumbers.is_valid_number(input_number)):
    #             raise ValidationError('Invalid Phone Number')
    #     except:
    #         input_number = phonenumbers.parse("+1"+field.data)
    #         if not (phonenumbers.is_valid_number(input_number)):
    #             raise ValidationError("Invalid Phone Number")