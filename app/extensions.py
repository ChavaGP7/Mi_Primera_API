from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


#cREAMOS UNA INSTANCIA QUE NOS AYUDARÁ A CONECTAR CON LA BD
db = SQLAlchemy()

jwt = JWTManager()

