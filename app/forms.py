from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, SubmitField
from wtforms.validators import InputRequired, Email

class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[InputRequired(message='este campo es obligatorio'), Email(message='Debe ser un email valido')], id='email')
    password = PasswordField("Contraseña", validators=[InputRequired(message='este campo es obligatorio')])
    submit = SubmitField("Iniciar sesión")