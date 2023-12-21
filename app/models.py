from app import db
from datetime import datetime


class Ciudad(db.Model):
    __tablename__ = "ciudades"
    id_ciudad = db.Column(db.Integer, primary_key=True)
    nombre_ciudad = db.Column(db.String(60), unique=True)
    
class Ocupacion(db.Model):
    __tablename__ = "ocupaciones"
    id_ocupacion = db.Column(db.Integer, primary_key=True)
    nombre_ocupacion = db.Column(db.String(50), unique = True)

class Cliente(db.Model):
    __tablename__ = "clientes"
    numero_documento = db.Column(db.Integer, primary_key=True, unique=True)
    nombre = db.Column(db.String(60))
    apellidos = db.Column(db.String(80))
    fecha_nacimiento = db.Column(db.Date)
    id_ciudad = db.Column(db.Integer, db.ForeignKey('ciudades.id_ciudad'))
    email = db.Column(db.String(100))
    telefono = db.Column(db.String(10))
    id_ocupacion = db.Column(db.Integer, db.ForeignKey('ocupaciones.id_ocupacion'))