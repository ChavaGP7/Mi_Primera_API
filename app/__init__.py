# Se va anecargar de montar el servidor
from flask import Flask # <-Este nos permite crear el servidor
from flask_restful import Api # Este nos permite crear la funcionalidad de la api
from .routes import APIRoutes
from .config import Config
from .extensions import db
# Creamos una funcion que configure el servidor

def configurar_app():
    # Variable que va a almacenar el servidor
    app = Flask(__name__)
    # Variable que va a almacenar la API
    # Le indicamos sobre que servidor va a interactuar
    app.config.from_object(Config)
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    api = Api(app)

# Configuramos la ruta y los recursos
    rutas = APIRoutes()
    rutas.init_api(api)
    
    return app