import email_validator
import wtforms as wtf
from flask_wtf import FlaskForm
from flask_wtf.file import FileField


class UserForm(FlaskForm):
  email = wtf.StringField(
    "Email", [wtf.validators.DataRequired(), wtf.validators.Email()]
    )
  password = wtf.PasswordField("Senha", [wtf.validators.DataRequired()])
  foto = FileField("Foto")

class LoginForm(FlaskForm):
  email = wtf.StringField("Email", [wtf.validators.DataRequired(), wtf.validators.Email()])
  password = wtf.PasswordField("Password", [wtf.validators.DataRequired()])
