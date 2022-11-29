#Importando  flask y algunos paquetes
from flask import Flask, render_template, request, redirect, url_for, flash, session, Blueprint
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from conexionBD import *  #Importando conexion BD
from funciones import *  #Importando mis Funciones
from formularios import formulario  #Importando mis Funciones
from routes import * #Vistas
# Models:
from models.ModelUser import Model_user
# Entities:
from models.entities.User import User

app = Flask(__name__)#Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
db = MySQL(app) #Inicializando la conexión a la BD
csrf = CSRFProtect()
login_manager_app = LoginManager(app)
app.register_blueprint(rutas) #Registrando mis rutas
app.register_blueprint(formulario) #Registrando mis rutas
@login_manager_app.user_loader
def load_user(id):
    return Model_user.get_by_id(db, id)

@app.route('/login', methods=['GET', 'POST'])
def login1():
    if 'conectado' in session:
        return render_template('public/modulo_login/login.html', data_login = datos_login())
    else:
        if request.method == 'POST':
            datos = request.form
            user = User(0, datos['Correo'], datos['Password'])
            logged_user = Model_user.login(db, user)
            if logged_user != None:
                if logged_user.Password:
                    login_user(logged_user)
                    
                    return redirect(url_for('rutas.inicio'))
                else:
                    flash("Invalid password...")
                    return render_template('public/modulo_login/login.html')
            else:
                flash("User not found...")
                return render_template('public/modulo_login/login.html')
        else:
            return render_template('public/modulo_login/login.html')
        
@app.errorhandler(404)
def not_found(error):
    if 'conectado' in session:
        return redirect(url_for('rutas.inicio'))
    else:
        return render_template('public/modulo_login/index.html') 
if __name__ == "__main__":
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.run(debug=True, port="4000", host="0.0.0.0")