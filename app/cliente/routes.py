from flask import render_template, redirect, url_for, flash, jsonify, request
from app.cliente import cliente
import app
from .forms import NewCliente, EditCliente

#Rutas
@cliente.route('/create', methods = ['GET', 'POST'])
def crear_cliente():
    if request.method == 'GET':
        c = app.models.Cliente()
        form = NewCliente()
        form.id_ciudad.choices = [(ciudad.id_ciudad, ciudad.nombre_ciudad) for ciudad in app.models.Ciudad.query.all()]
        form.id_ocupacion.choices = [(ocupacion.id_ocupacion, ocupacion.nombre_ocupacion) for ocupacion in app.models.Ocupacion.query.all()]
        return render_template('new_cliente.html', form=form)

    elif request.method == 'POST':
        try:
            data = request.json
            print(data)
            nuevo_cliente = app.models.Cliente(
            numero_documento=data['numero_documento'],
            nombre=data['nombre'],
            apellidos=data['apellidos'],
            fecha_nacimiento=data['fecha_nacimiento'],
            id_ciudad=data['id_ciudad'],
            email=data['email'],
            telefono=data['telefono'],
            id_ocupacion=data['id_ocupacion']
            )
            app.db.session.add(nuevo_cliente)
            app.db.session.commit()
            print('Cliente guardado')
            return jsonify({'mensaje': 'Cliente registrado correctamente'})
        
        except Exception as ex:
            return jsonify({'mensaje': f'Error al registrar el cliente. Detalles: {str(ex)}'})