from werkzeug.security import check_password_hash
from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id, correo, password, nombre="",apellido="",direccion="",ciudad="",pais="") -> None:
        self.id = id
        self.Correo = correo
        self.Password = password
        self.Nombre = nombre
        self.Apellido = apellido
        self.Direccion = direccion
        self.Ciudad = ciudad
        self.Pais = pais
        
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)