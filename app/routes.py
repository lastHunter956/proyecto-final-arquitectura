from flask import Flask, render_template, request, redirect, url_for, flash,Blueprint,session
from flask_login import LoginManager, login_user, logout_user, login_required
import requests #se usa para hacer peticiones a la api
from funciones import *  #Importando mis Funciones

rutas = Blueprint("rutas", __name__)
#Redireccionando cuando la página no existe
    
#Creando mi Decorador para el Home
@rutas.route('/')
def inicio():
    if 'conectado' in session:
        return render_template('public/dashboard/index.html', data_login = datos_login())
    else:
        return render_template('public/modulo_login/index.html')   
@rutas.route('/vehiculos_nuevos')
def vehiculos_nuevos():
    if 'conectado' in session:
        return render_template('public/dashboard/pages/vehi_nuevos.html', data_login = datos_login())
    else:
        return render_template('public/modulo_login/vehi_nuevos.html')  
@rutas.route('/vehiculos_usados')
def vehiculos_usados():
    if 'conectado' in session:
        return render_template('public/dashboard/pages/vehi_usados.html', data_login = datos_login())
    else:
        return render_template('public/modulo_login/vehi_usados.html')  
# Cerrar session del usuario
@rutas.route('/logout')
def logout():
    msg_cerrado = ''
    # Eliminar datos de sesión, esto cerrará la sesión del usuario
    session.pop('conectado', None)
    logout_user()
    msg_cerrado ="La sesión fue cerrada correctamente"
    return render_template('public/modulo_login/index.html', msjAlert = msg_cerrado, typeAlert=1)

@rutas.route('/compras')
@login_required
def compras():
    return render_template('public/dashboard/pages/compras.html', data_login = datos_login())

@rutas.route('/protect')
@login_required
def protect():
    return "<h1>Protegido check</h1>"
