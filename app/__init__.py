from flask import Flask, session, redirect, url_for
from .config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.cliente import cliente
from flask_bootstrap import Bootstrap
from flask import render_template
from app.forms import LoginForm


#Inicializador del objeto flask
app = Flask(__name__)
app.config.from_object(Config)

# Objeto para bootstrap
bootstrap = Bootstrap(app)

#iniciacializar a continuacion el objeto SQLalchemy
db=SQLAlchemy(app)
Migrate(app , db)

#Registrar modulos (blueprints)
app.register_blueprint(cliente)

from .models import Ciudad, Ocupacion, Cliente

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        cliente = Cliente.query.filter_by(email=email, password=password).first()

        if cliente:
            id_cliente = cliente.numero_documento
            session['nombre'] = cliente.nombre
            session['id_ocupacion'] = cliente.id_ocupacion

            print('Inicio de sesión exitoso')

            if cliente.id_ocupacion == 1:
                return redirect(url_for('cliente.home', id_cliente=id_cliente))
            else:
                return 'No tienes permisos'
        else:
            return 'Credenciales incorrectas'

    return render_template('login.html', form=form)