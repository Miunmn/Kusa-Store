from itertools import product
from os import access, name
import datetime

from flask_sqlalchemy import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Float, String, Sequence, DateTime, ForeignKey, Table, Text, Boolean
from sqlalchemy.sql.expression import null

from forms import RegisterForm, ProductForm

#from flask_user import current_user, login_required, roles_required, UserManager, UserMixin

import bcrypt
from flask_rbac import RoleMixin

from flask import Flask, render_template, flash, request, redirect, sessions, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_rbac import RBAC


from flask_login import login_required, current_user, login_user, logout_user , AnonymousUserMixin
from flask_login import LoginManager
from flask_login import current_user

from flask_wtf import CSRFProtect


csrf = CSRFProtect()

app = Flask(__name__, static_url_path='/static')

app.config.from_pyfile('config.py')

login_manager = LoginManager()
login_manager.init_app(app)

csrf.init_app(app)
db = SQLAlchemy(app)
#rbac = RBAC(app)

migrate = Migrate(app, db)

from flask import session
    
Base = db.Model

ACCESS = {
    'client': 1,
    'admin': 2
}
#user_manager = UserManager(app, db, Usuario)

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False, server_default='')
    access = Column(Integer, nullable=False)
    compras = relationship('Compra', back_populates='usuario', lazy=True)

    def __init__(self, username, password,access):
        self.username = username
        self.password = password
        self.access = access

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def get_access(self):
        return str(self.access)

    def __repr__(self):
        return '<name - {}>'.format(self.username)
    
class Categoria(Base):
    __tablename__ = 'categoria'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    subcategorias = relationship(
        'Subcategoria', back_populates='categoria', lazy=True)


subcategoria_producto = Table(
    'subcategoria_producto', Base.metadata,
    Column('subcategoria_id', Integer, ForeignKey('subcategoria.id')),
    Column('producto_id', Integer, ForeignKey('producto.id'))
)


class Subcategoria(Base):
    __tablename__ = 'subcategoria'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    categoria_id = Column(Integer, ForeignKey('categoria.id'))

    # Many to one relationship with Categoria
    categoria = relationship('Categoria', back_populates='subcategorias')

    # For Many to Many relationship with Producto
    productos = relationship(
        'Producto', secondary=subcategoria_producto, back_populates='subcategorias')


# Many to Many between Compra - Producto
compra_producto = Table(
    'compra_producto', Base.metadata,
    Column('compra_id', Integer, ForeignKey  ('compra.id')),
    Column('producto_id', Integer, ForeignKey('producto.id'))
)


class Producto(Base):
    __tablename__ = 'producto'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    precio = Column(Float, nullable=False)
    descripcion = Column(String(255))
    img_url =  Column(String(255),nullable=False)
    stock = Column(Integer)

    # For Many to Many relationship with Subcategoria
    subcategorias = relationship(
        'Subcategoria', secondary=subcategoria_producto, back_populates="productos")

    # For Many to Many relationship with Compra
    compras = relationship(
        'Compra', secondary=compra_producto, back_populates="productos")


class Compra(Base):
    __tablename__ = 'compra'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    fecha = Column(DateTime, nullable=False)

    # Many to one relationship with Usuario
    usuario = relationship('Usuario', back_populates="compras")

    # For Many to Many relationship with producto
    productos = relationship(
        'Producto', secondary=compra_producto, back_populates="compras")

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.filter(Usuario.id == str(user_id)).first()

# User Create
def create_user():
    pass


# User Retrieve
def retrieve_user():
    pass


# User Update
def update_user():
    pass

def ifadmin(user):
    return user.access == ACCESS['admin']

def ifclient(user):
    return user.access == ACCESS['client']

# only for admins
# Product Create
#@roles_required('Admin')
@app.route('/createproduct', methods=['GET','POST'])
def create_product():
    mensaje = None
    user = current_user
    if user.is_authenticated:
        if ifclient(user):
            return redirect(url_for('.index'))
        if request.method == 'POST':
            if ifadmin(user):
                producto = Producto(
                    nombre=request.form['nombre'],
                    precio=request.form['precio'],
                    descripcion=request.form['descripcion'],
                    stock=request.form['stock']
                    #agregar img_url
                )
                db.session.add(producto)
                db.session.commit()
                mensaje = "Producto agregado"
                return render_template('agregarproducto.html', mensaje=mensaje)
        return render_template('agregarproducto.html', mensaje=mensaje)
    else:
        return redirect(url_for('.index'))

# Product Retrieve
def retrieve_product():
    pass

@app.route('/updateproduct', methods=['GET','POST'])
def update_product():
    mensaje = None
    user = current_user
    if user.is_authenticated:
        if ifclient(user):
            return redirect(url_for('.index',mensaje=mensaje))
        if request.method == 'POST':
            if request.form['nombre'] == "":
                mensaje = "Especifique el nombre del producto"
            else:
                if ifadmin(user):
                    name = request.form['nombre']
                    product = Producto.query.filter_by(nombre=name).first()
                    if product is not None:
                        if request.form['descripcion'] != "":
                            product.descripcion = request.form['descripcion']
                        if request.form['precio'] != "":
                            product.precio = request.form['precio']
                        if request.form['stock'] != "":
                            product.stock = request.form['stock']
                        db.session.commit()
                        mensaje = "Producto actualizado"
                    else:
                        mensaje = "Producto inexistente"
                    return render_template('actualizar.html',mensaje=mensaje)
        return render_template('actualizar.html',mensaje=mensaje)
    else:
        return redirect(url_for('.index'))


# only for admins
@app.route('/deleteproduct', methods=['GET'])
def delete_product():
    if request.method == 'GET':
        user = current_user
        mensaje = None
        if user.is_authenticated:
            if ifadmin(user):
                nombre = request.args['name']
                producto = Producto.query.filter_by(nombre=nombre).first()
                if producto is not None:
                    db.session.delete(producto)
                    db.session.commit()
                    mensaje = "Eliminado con éxito"
                    return redirect(url_for('.index', mensaje=mensaje))
        return redirect(url_for('.index', mensaje=mensaje))

@app.route('/singleproduct', methods=['GET'])
def singleproduct():
    if request.method == 'GET':
        mensaje = None
        name = request.args['name']
        producto = Producto.query.filter_by(nombre=name).first()
        if producto is None:
            mensaje = "No existe producto"
        else:
            return render_template('shop-single.html', mensaje=mensaje, producto=producto)
        return redirect(url_for('.index', mensaje=mensaje))
    return redirect(url_for('.index'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out.')
    return redirect(url_for('.login'))

@app.route('/')
def index():
    allproducts = Producto.query.all()
    ifcliente_ = ""
    ifadmin_ = ""
    user = current_user
    if user.is_authenticated:
        print("USERRR USUARIO")
        if ifadmin(user):
            print("USER ADMIN")
            ifadmin_ = "ADMIN"
        elif ifclient(user):
            print("USER CLIENTE")
            ifcliente_ = "CLIENTE"
    else:
        print(user)
    return render_template(
        'shop.html', 
        allproducts=allproducts,
        ifadmin=ifadmin_,
        ifcliente=ifcliente_
    )

'''
@app.route('/signupadmin', methods=['GET', 'POST'])
def signup():
    error = None
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user_ = Usuario.query.filter_by(username=request.form['username']).first()
            if user_ is not None:
                error = 'Username ya utilizado'
            else:
                password = request.form['password']
                user = Usuario(
                    username=request.form['username'],
                    password=password,
                    access=ACCESS['admin']
                )                
                db.session.add(user)
                db.session.commit()
            
                login_user(user)
            return redirect(url_for('.index'))
        else:
            flash(form.errors)
    else:
        error = 'Invalid data'       
    return render_template('register.html',  error=error)'''


@app.route('/signup', methods=['GET', 'POST'])
def signupcliente():
    error = None
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user_ = Usuario.query.filter_by(username=request.form['username']).first()
            if user_ is not None:
                error = 'Username ya utilizado'
            else:
                user = Usuario(
                username=request.form['username'],
                password=request.form['password'],
                access=ACCESS['client']
                )
                db.session.add(user)
                db.session.commit()            

                login_user(user)
            return redirect(url_for('.index'))
        else:
            flash(form.errors)
    else:
        error = 'Invalid data'       
    return render_template('register.html', error=error)

@app.route('/login', methods=['GET','POST'])
def login():
    errormessage = ""
    user = current_user
    if user.is_authenticated:
        return redirect(url_for('.index'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Usuario.query.filter_by(username=username).first()
        if user is None:
            errormessage = 'No existe el usuario'
        else:
            if password == user.password:
                login_user(user)
                return redirect(url_for('.index'))
            else:
                errormessage = "Contraseña equivocada"
    return render_template('login.html', errormessage=errormessage)

if __name__ == '__main__':
    db.create_all()
    #setup()
    app.run(host="127.0.0.1", port=8080, debug=True)