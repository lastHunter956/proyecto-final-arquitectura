from flask import render_template, redirect, url_for, flash,Blueprint,session,request,Blueprint
from funciones import *  #Importando mis Funciones
import requests #se usa para hacer peticiones a la api

from flask_login import LoginManager, login_user, logout_user, login_required
formulario = Blueprint("formulario", __name__)
#Redireccionando cuando la página no existe
@formulario.route('/signup', methods=['GET', 'POST'])
def signup():
    datos = request.form
    if request.method == 'POST':
        print("Datos: ", datos["Cedula"])
        params = {"Apellido": datos["Apellido"],"Correo": datos["Correo"],
                  "Cedula": datos["Cedula"],"Ciudad": datos["Ciudad"],
                  "Direccion": datos["Direccion"],"Nombre": datos["Nombre"],
                  "Pais": datos["Pais"],"Contraseña": datos["password"]
            }
        response = requests.post('https://api-crear-cuenta.onrender.com/signup', json=params)
        if response.status_code == 200:
            return render_template('public/modulo_login/login.html')
        return render_template('public/dashboard/index.html')  
    return render_template('public/modulo_login/signup.html')
@formulario.route('/perfil', methods=['GET', 'POST'])
@login_required
def actualizar_perfil():
    datos = request.form
    if request.method == 'POST':
        print("Datos: ", session["Cedula"])
        params = {"Apellido": datos["Apellido"],
                  "Correo": datos["Correo"],
                  "Ciudad": datos["Ciudad"],
                  "Direccion": datos["Direccion"],
                  "Nombre": datos["Nombre"],
                  "Pais": datos["Pais"],
            }
        url = 'https://api-crear-cuenta.onrender.com/signup/'+session['Cedula']
        response = requests.put(url, json=params)
        if response.status_code == 200:
            return render_template('public/dashboard/perfil.html')
        return render_template('public/dashboard/index.html')  
    return render_template('public/dashboard/perfil.html')
@formulario.route('/vender', methods=['GET', 'POST'])
@login_required
def vender_vehiculo():
    datos = request.form
    if request.method == 'POST':
        print("Datos: ", session["Cedula"])
        params = {
            "Caracteristica": datos["Caracteristica"],
            "Modelo": datos["Marca"],
            "Nombre": datos["Nombre"],
            "Precio": float(datos["Precio"]),
            "Descripcion": datos["Descripcion"],
            "Imagen": datos["Imagen"]
            }
        url = 'https://api-ventas.onrender.com/venta/'+session['Correo']
        response = requests.post(url, json = params)
        if response.status_code == 200:
            return render_template('public/dashboard/pages/vender.html')
        return render_template('public/dashboard/index.html')  
    return render_template('public/dashboard/pages/vender.html')