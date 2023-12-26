from app import db
from datetime import datetime
from sqlalchemy.orm import relationship


class Ciudad(db.Model):
    __tablename__ = "ciudades"
    id_ciudad = db.Column(db.Integer, primary_key=True)
    nombre_ciudad = db.Column(db.String(60), unique=True)
    clientes = relationship("Cliente", back_populates="ciudad")
    
class Ocupacion(db.Model):
    __tablename__ = "ocupaciones"
    id_ocupacion = db.Column(db.Integer, primary_key=True)
    nombre_ocupacion = db.Column(db.String(50), unique = True)
    clientes = relationship("Cliente", back_populates="ocupacion")


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
    viable = db.Column(db.String(5))
    password = db.Column(db.String(20))
    
    # Para poder listar los datos con Rest
    def serialize(self):
        return {
            'id_cliente': self.numero_documento,
            'nombre': self.nombre,
            'apellidos': self.apellidos,
            'fecha_nacimiento': self.fecha_nacimiento,
            'id_ciudad': self.id_ciudad,
            'email': self.email,
            'telefono': self.telefono,
            'id_ocupacion': self.id_ocupacion
        }
        
    ciudad = relationship("Ciudad", back_populates="clientes")
    ocupacion = relationship("Ocupacion", back_populates="clientes")