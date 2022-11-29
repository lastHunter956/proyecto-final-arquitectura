from .entities.User import User
from flask import session

class Model_user():

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT Cedula, Correo, Contraseña , Nombre ,Apellido, Direccion, Ciudad, Pais  FROM heroku_978ea61906c2949.usuario  
                    WHERE Correo = '{}'""".format(user.Correo)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], User.check_password(row[2], user.Password), row[3],row[4],row[5],row[6],row[7])
                session['conectado'] = True
                session['Cedula'] = user.id
                session['Nombre'] = user.Nombre
                session['Apellido'] = user.Apellido
                session['Direccion'] = user.Direccion
                session['Ciudad'] = user.Ciudad
                session['Pais'] = user.Pais
                session['Correo'] = user.Correo                
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT Cedula, Correo, Contraseña , Nombre ,Apellido, Direccion, Ciudad, Pais FROM heroku_978ea61906c2949.usuario WHERE Cedula = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
