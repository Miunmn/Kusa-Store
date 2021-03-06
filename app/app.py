import time
import bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, jsonify, request, flash, redirect, url_for
from flask_login import login_required, current_user, login_user, logout_user
from flask_login import LoginManager
from flask_login import current_user
import os
from flask_wtf import FlaskForm
from sqlalchemy.sql.base import NO_ARG
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_wtf.csrf import CsrfProtect
import json


from forms import RegisterForm, ProductForm
csrf = CsrfProtect()

DBUSER = 'proyectodbp'
DBPASS = 'password'
DBHOST = 'db'
DBPORT = '5432'
DBNAME = 'dbpdatabase'

app = Flask(__name__,
    static_url_path='/static'
    )
csrf.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=DBUSER,
        passwd=DBPASS,
        host=DBHOST,
        port=DBPORT,
        db=DBNAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TESTING'] = True
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)



class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    hash = db.Column(db.Text, nullable=False)
    #password = db.Column(db.String)

    def __init__(self,name, username, hash):
        self.name = name
        self.username = username
        self.hash = hash

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<name - {}>'.format(self.name)

class Producto(db.Model):
    __tablename__ = 'producto'
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(50))
    nombre = db.Column(db.String(50))
    descripcion = db.Column(db.String(50))
    precio = db.Column(db.Float)
    url = db.Column(db.String(512))

    def __init__(self, categoria, nombre, descripcion, precio, url):
        self.categoria = categoria
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.url = url

def database_initialization_sequence():
    db.create_all()
    db.session.commit()
    #creacion de usuarios ya que siempre que se detiene el docker se borra todo
    '''user1 = User( "Esteban","ZzAZza","testpassword")
    user2 = User("Jose","josedlz","testpassword")
    user3 = User("alien","idgaf","testpassword")'''
    #db.session.add_all([user1,user2,user3])



@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == str(user_id)).first()

@app.route('/',methods=['GET'])
def landing():
    return render_template('index.html')

@app.route('/catalogo', methods=['GET'])
def viewcatalogo():
        return render_template('catalogo.html')

@app.route('/agregarproducto', methods=['GET','POST'])
@login_required
def agregarproducto():
    form = ProductForm(request.form)
    if request.method == 'POST':
        print(form.errors)
        if form.validate_on_submit():
            new_product = Producto(
            categoria=request.form['categoria'],
            nombre=request.form['nombre'],
            precio=request.form['precio'],
            descripcion=request.form['descripcion'],
            url=request.form['url']
            )

            db.session.add(new_product)
            db.session.commit()
            flash("Producto agregado!")
        print(form.errors)
    return render_template('agregado.html')

@app.route('/eliminarproducto',methods=['GET','POST'])
@login_required
def eliminarproducto():
    producto = None
    delete_message = None
    productodatos = {}
    print("request.method: ",request.method)
    if request.method == 'POST':
        print("request.method == 'POST':")
        idtodelete = request.form['id']
        print("idtodelete: ",idtodelete)
        producto = Producto.query.filter_by(id=idtodelete).first()
        if producto is not None:
            productodatos['nombre'] = producto.nombre
            productodatos['categoria'] = producto.categoria
            Producto.query.filter_by(id=idtodelete).delete()
            #db.session.delete(new_product)
            db.session.commit()
            delete_message = "Producto eliminado con ??xito!"
        else:
            delete_message = "No existe producto con tal id proporcionado"
    return render_template('eliminar.html',delete_message=delete_message,productodatos=productodatos)

@app.route('/actualizarproducto',methods=['GET','POST'])
@login_required
def actualizarproducto():
    if request.method == "POST" and request.form['id'] is not None:
        productotoupdate = Producto.query.filter_by(id=request.form['id']).first()
        if productotoupdate is not None:
            if request.form['categoria'] != "":
                productotoupdate.categoria = request.form['categoria']
            if request.form['precio'] != "":
                productotoupdate.precio = request.form['precio']
            if request.form['nombre'] != "":
                productotoupdate.nombre = request.form['nombre']
            if request.form['descripcion'] != "":
                productotoupdate.nombre = request.form['descripcion']
            db.session.commit()
            message = "Cambios realizados al producto"
        else:
            message = "El id proporcionado no le pertenece a ninguna entrada"
    else:
        message = "Proporcione un id"
    return render_template('actualizar.html',message=message)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            password = request.form['password']
            hashedvalue = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            user = User(
                name=request.form['name'],
                username=request.form['username'],
                hash=hashedvalue
            )
            
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return render_template('catalogo.html')
        else:
            flash(form.errors)
    else:
        error = 'Invalid data'       
    return render_template('register.html',  error=error)

# Login view
@app.route('/login', methods=['GET','POST'])
def login():
    errormessage = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user is None:
            errormessage = 'No existe el usuario'
        else: 
            if bcrypt.checkpw(password.encode('utf-8'), user.hash):
                login_user(user)
                return redirect(url_for('.viewcatalogo'))
            else:
                errormessage = "Contrase??a equivocada"
    return render_template('login.html', errormessage=errormessage)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out.')
    return redirect(url_for('.login'))

if __name__ == '__main__':
    dbstatus = False
    while dbstatus == False:
        try:
            db.create_all()
        except:
            time.sleep(2)
        else:
            dbstatus = True
    database_initialization_sequence()
    app.run(debug=True, host='0.0.0.0')
