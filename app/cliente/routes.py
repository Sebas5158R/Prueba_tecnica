from flask import render_template, flash, jsonify, request, session, redirect, url_for
from app.cliente import cliente
import app
from .forms import ClienteForm
from datetime import datetime

#Rutas
# Listar clientes
@cliente.route('/listar/<int:id_cliente>', methods=['GET'])
def listar_clientes(id_cliente):
    clientes = app.models.Cliente.query.all()
    if 'nombre_usuario' in session and session.get('id_ocupacion') == 1:
        clientes = app.models.Cliente.query.all()
    
    elif 'application/json' in request.headers.get('Accept'):
        clientes = app.models.Cliente.query.all()
        return jsonify({'Clientes': [cliente.serialize() for cliente in clientes]})
    
    return render_template('listar_clientes.html', clientes=clientes)


# Crear clientes
@cliente.route('/create', methods = ['GET', 'POST'])
def crear_cliente():
    if request.method == 'GET':
        c = app.models.Cliente()
        form = ClienteForm()
        form.id_ciudad.choices = [(ciudad.id_ciudad, ciudad.nombre_ciudad) for ciudad in app.models.Ciudad.query.all()]
        form.id_ocupacion.choices = [(ocupacion.id_ocupacion, ocupacion.nombre_ocupacion) for ocupacion in app.models.Ocupacion.query.all()]
        return render_template('new_cliente.html', form=form, c=c)

    elif request.method == 'POST':
        try:
            c = app.models.Cliente()
            data = request.json
            print(data)
            fecha = data['fecha_nacimiento']
            fecha_nacimiento = datetime.strptime(fecha, "%Y-%m-%d" )
            edad = datetime.now().year - fecha_nacimiento.year
            print('Edad cliente:', edad)
            if edad > 17 and edad < 66:
                print("Es viable")
                edad = "Si"
            else:
                edad = "No"
            nuevo_cliente = app.models.Cliente(
                numero_documento=data['numero_documento'],
                nombre=data['nombre'],
                apellidos=data['apellidos'],
                fecha_nacimiento=data['fecha_nacimiento'],
                id_ciudad=data['id_ciudad'],
                email=data['email'],
                telefono=data['telefono'],
                id_ocupacion=data['id_ocupacion'],
                viable=edad
            )
            app.db.session.add(nuevo_cliente)
            app.db.session.commit()
            print('Cliente guardado')
            return jsonify({'mensaje': 'Cliente registrado correctamente'})
        
        except Exception as ex:
            return jsonify({'mensaje': f'Error al registrar el cliente. Detalles: {str(ex)}'})
        

# Editar clientes
@cliente.route('/update/<id_cliente>', methods=['GET', 'POST', 'PUT'])
def actualizar_cliente(id_cliente):
    c = app.models.Cliente.query.get_or_404(id_cliente)
    form = ClienteForm(obj=c)
    form.id_ciudad.choices = [(ciudad.id_ciudad, ciudad.nombre_ciudad) for ciudad in app.models.Ciudad.query.all()]
    form.id_ocupacion.choices = [(ocupacion.id_ocupacion, ocupacion.nombre_ocupacion) for ocupacion in app.models.Ocupacion.query.all()]

    if request.method == 'POST' or request.method == 'PUT':
        try:
            data = request.json
            form.populate_obj(c)
            print(data)
            fecha = data['fecha_nacimiento']
            fecha_nacimiento = datetime.strptime(fecha, "%Y-%m-%d" )
            edad = datetime.now().year - fecha_nacimiento.year
            print('Edad cliente:', edad)
            if edad > 17 and edad < 66:
                print("Es viable")
                c.viable = "Si"
            else:
                print("No es viable")
                c.viable = "No"
            app.db.session.commit()
            print('Cliente actualizado')
            return jsonify({'mensaje': 'Cliente editado exitosamente'})
        except Exception as ex:
            return jsonify({'mensaje': f'Error al editar al cliente. Detalles: {str(ex)}'})

    return render_template('new_cliente.html', form=form, c=c)


# Eliminar clientes
@cliente.route('/delete/<int:id_cliente>', methods=['GET', 'POST', 'DELETE'])
def eliminar_cliente(id_cliente):
    id_cliente = app.models.Cliente.query.get_or_404(id_cliente)
    eliminar = id_cliente
    try:
        if eliminar:
            app.db.session.delete(eliminar)
            app.db.session.commit()
            flash(f'Cliente {id_cliente} eliminado correctamente', 'success')
            return jsonify({'mensaje': 'Cliente eliminado correctamente'})
    except Exception as ex:
        return jsonify({'mensaje': f'Error al eliminar al cliente. Detalles: {str(ex)}'})
    
# Home
@cliente.route('/home/<int:id_cliente>')
def home(id_cliente):
    print("id cliente: ", id_cliente)
    cliente = app.models.Cliente.query.get(id_cliente)
    return render_template('home.html', cliente = cliente)

# Cerrar sesión y limpiar la session
@cliente.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))