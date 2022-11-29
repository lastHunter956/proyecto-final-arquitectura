from flask import Flask, session
from conexionBD import * 

from flask_mysqldb import MySQL

servidor = Flask(__name__)
db = MySQL(servidor)
def datos_login():
    info_login = {
        "cedula":session['Cedula'],
        "direccion":session['Direccion'],
        "nombre":session['Nombre'],
        "apellido":session['Apellido'],
        "ciudad":session['Ciudad'],
        "pais":session['Pais'],
        "correo":session['Correo'],
    }
    return info_login

def perfil_usuario():
    conexion = db.connection.cursor()
    cursor = conexion.cursor(dictionary=True)
    id = session['Cedula']
    consulta  = ("select * from heroku_978ea61906c2949.usuario where Cedula = '%s'" % (id,))
    cursor .execute(consulta)
    datos_usuario = cursor.fetchone() 
    cursor.close() #cerrando conexion SQL
    conexion.close() #cerrando conexion de la BD
    return datos_usuario



