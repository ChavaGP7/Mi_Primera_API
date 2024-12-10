from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__= 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    telefono = db.Column(db.String, nullable=False)
    password = db.Column(db.Text(), nullable=False)

    def hashear_password(self, password):
        self.password = generate_password_hash(password)
    
    def verificar_password(self, password):

        return check_password_hash(self.password, password)
    
    

    #Método de la Clase User
    def save(self):
        # Crea una sesión con mi base de datos
        db.session.add(self)
        #En esa conexion guardamos los cambios y la cerramos
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()




