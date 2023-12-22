from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, DateField, SelectField, SubmitField
from wtforms.validators import InputRequired, Length, Email

class ClienteForm():
    numero_documento = IntegerField("Número de documento", validators=[InputRequired(message='Este campo es obligatorio')], id='numero_documento')
    nombre = StringField("Nombre", validators=[InputRequired(message='Este campo es obligatorio')], id='nombre')
    apellidos = StringField("Apellidos", validators=[InputRequired(message='Este campo es obligatorio')], id='apellidos')
    fecha_nacimiento = DateField("Fecha de nacimiento", validators=[InputRequired(message=('Requerido'))], id='fecha_nacimiento') 
    id_ciudad = SelectField("Ciudad", coerce=int, id='id_ciudad')
    email = EmailField("Email", validators=[InputRequired(message='este campo es obligatorio'), Email(message='Debe ser un email valido')], id='email')
    telefono = IntegerField("Número de telefono", validators=[InputRequired(message='Este campo es obligatorio')], id='telefono')
    id_ocupacion = SelectField("Ocupación", coerce=int)
    
class NewCliente(FlaskForm, ClienteForm):
    submit = SubmitField("Registrar", render_kw={'onclick': 'enviarFormulario()'})
    
class EditCliente(FlaskForm, ClienteForm):
    submit = SubmitField("Guardar", render_kw={'onclick': 'enviarFormulario()'})