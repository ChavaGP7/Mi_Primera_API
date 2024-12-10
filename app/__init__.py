# Se va anecargar de montar el servidor
from flask import Flask, jsonify # <-Este nos permite crear el servidor
from flask_restful import Api # Este nos permite crear la funcionalidad de la api
from .routes import APIRoutes
from .config import Config
from flask_jwt_extended.exceptions import NoAuthorizationError, InvalidHeaderError
from .extensions import db, jwt
# Creamos una funcion que configure el servidor

def configurar_app():
    # Variable que va a almacenar el servidor
    app = Flask(__name__)
    # Variable que va a almacenar la API
    # Le indicamos sobre que servidor va a interactuar
    app.config.from_object(Config)
    
    db.init_app(app)

    jwt.init_app(app)
    
    with app.app_context():
        db.create_all()

    api = Api(app)

# Configuramos la ruta y los recursos
    rutas = APIRoutes()
    rutas.init_api(api)

    # Manejador para cuando no se proporciona un token
    @app.errorhandler(NoAuthorizationError)
    def handle_no_token(e):
       return jsonify({
          "message": "Se requiere un token de autorización.",
          "error": str(e)
          }), 401

  # Manejador para cuando el token es inválido o tiene un formato incorrecto
    @app.errorhandler(InvalidHeaderError)
    def handle_invalid_token(e):
       return jsonify({
          "message": "Token inválido o mal formado.",
          "error": str(e)
          }), 422

  # Manejador para cuando el token ha expirado
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({
          "message": "El token ha expirado.",
          "error": "token_expired"
          }), 401

    
    return app