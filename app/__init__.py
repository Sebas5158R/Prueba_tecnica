from flask import Flask
from .config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.cliente import cliente
from flask_bootstrap import Bootstrap
from flask import render_template

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