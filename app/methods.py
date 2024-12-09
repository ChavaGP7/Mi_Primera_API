from .models.usuarios import User
from flask_jwt_extended import create_access_token

from datetime import timedelta

def user_register(nombre, email, telefono, password):
    
    usuario_existente = User.query.filter_by(email=email).first()

    if usuario_existente is not None:
        return {'Error': 'El usuario ya está registrado :('}, 403
    

    
    nuevo_usuario = User(nombre=nombre, email=email, telefono=telefono)

    nuevo_usuario.hashear_password(password=password)


    nuevo_usuario.save()

    return {
        'status': 'Usuario registrado',
        'email' : email,
        'telefono' : telefono

    }, 200


def user_login(correo, password):

    usuario_existente = User.query.filter_by(email=correo).first()

    if usuario_existente is None:
        return{'Status': 'El correo no está registrado'}, 500
    #Verificamos que la contraseña coincida
    elif usuario_existente.verificar_password(password=password):
        caducidad = timedelta(minutes=2)

        token_acceso = create_access_token(identity=usuario_existente.nombre, expires_delta=caducidad)

        return {
            'Status': 'Sesión iniciada',
            'Token' : token_acceso
            }, 200
    
    else:
        return {'Status': 'La contraseña no coincide'}, 500
        


