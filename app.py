from sqlalchemy import Column, Integer, Float, String, Sequence, DateTime, ForeignKey, Table, Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.exc import IntegrityError


from flask import Flask, render_template, flash, request, redirect, url_for, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.base import NO_ARG
from flask_migrate import Migrate


from flask_login import login_required, current_user, login_user, logout_user
from flask_login import LoginManager
from flask_login import current_user

from flask_wtf import CSRFProtect
from datetime import datetime

from forms import *


csrf = CSRFProtect()

app = Flask(__name__, static_url_path='/static')

app.config.from_pyfile('config.py')

login_manager = LoginManager()
login_manager.init_app(app)

csrf.init_app(app)
db = SQLAlchemy(app)

migrate = Migrate(app, db)

Base = db.Model

ACCESS = {
    'client': 1,
    'admin': 2
}


class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False, server_default='')
    access = Column(Integer, nullable=False)
    balance = Column(Integer, nullable=False)
    compras = relationship('Compra', back_populates='usuario', lazy=True)

    def __init__(self, username, password, access, balance):
        self.username = username
        self.password = password
        self.access = access
        self.balance = balance

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def is_admin(self):
        return self.access == ACCESS['admin']
    
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
    Column('compra_id', Integer, ForeignKey('compra.id')),
    Column('producto_id', Integer, ForeignKey('producto.id'))
)


class Producto(Base):
    __tablename__ = 'producto'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    precio = Column(Float, nullable=False)
    descripcion = Column(String(255))
    img_url = Column(String(255), nullable=False)
    stock = Column(Integer)

    # For Many to Many relationship with Subcategoria
    subcategorias = relationship(
        'Subcategoria', secondary=subcategoria_producto, back_populates="productos")

    # For Many to Many relationship with Compra
    compras = relationship(
        'Compra', secondary=compra_producto, back_populates="productos")

    def to_json(self):
        return {k:v for k, v in self.__dict__.items() if k != '_sa_instance_state'} 


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


@app.errorhandler(500)
def serverError(error):
    return render_template('500.html')


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.filter(Usuario.id == str(user_id)).first()


def is_admin(user):
    return user is not None and user.is_authenticated and user.access == ACCESS['admin']


def is_client(user):
    return user is not None and user.is_authenticated and user.access == ACCESS['client']


def mensajeforms(errorforms):
    retorno = ""
    if errorforms.get('nombre') is not None:
        retorno = retorno + " Nombre"
    if errorforms.get('descripcion') is not None:
        retorno = retorno + " Descripcion"
    if errorforms.get('stock') is not None:
        retorno = retorno + " Stock"
    if errorforms.get('precio') is not None:
        retorno = retorno + " Precio"
    if errorforms.get('img_url') is not None:
        retorno = retorno + " Url"
    return retorno



@app.route('/createproduct', methods=['GET', 'POST'])
def create_product():
    user = current_user
    if not user.is_authenticated:
        return redirect(url_for('.index'))

    if not user.is_admin:
        return redirect(url_for('.index'))

    if request.method == 'GET':
        return render_template('agregarproducto.html', mensaje=None)

    if request.method != 'POST':
        abort(500)

    flask_form = CreateProductForm(request.form)

    if not flask_form.validate_on_submit():
        mensaje = "Los siguiente campos son incorrectos: "
        mensaje = mensaje + mensajeforms(flask_form.errors)
        return render_template('agregarproducto.html', mensaje=mensaje)

    try:
        producto = Producto(
            nombre=request.form['nombre'],
            precio=request.form['precio'],
            descripcion=request.form['descripcion'],
            stock=request.form['stock'],
            img_url=request.form['img_url']
        )
        db.session.add(producto)
        db.session.commit()
        return render_template('agregarproducto.html', mensaje='Producto agregado')

    except Exception:
        db.session.rollback()
        abort(500)


@app.route('/updateproduct', methods=['GET', 'POST'])
def update_product():
    mensaje = None
    user = current_user
    if user.is_authenticated:
        if is_client(user):
            return redirect(url_for('.index', mensaje=mensaje))
        if request.method == 'POST':
            if request.form['nombre'] == "":
                mensaje = "Especifique el nombre del producto"
            else:
                if is_admin(user):
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
                    return render_template('actualizar.html', mensaje=mensaje)
        return render_template('actualizar.html', mensaje=mensaje)
    else:
        return redirect(url_for('.index'))


# only for admins
@app.route('/deleteproduct', methods=['GET'])
def delete_product():
    if request.method == 'GET':
        user = current_user
        mensaje = None
        if user.is_authenticated:
            if is_admin(user):
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
            return redirect(url_for('.index', mensaje=mensaje), code=404)
        else:
            return render_template('shop-single.html', mensaje=mensaje, producto=producto)

    return redirect(url_for('.index'), code=400)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out.')
    return redirect(url_for('.login'))


@app.route('/shop')
def shop():
    allproducts = Producto.query.all()
    if not current_user.is_authenticated:
        return redirect(url_for('.login'))

    return render_template('shop.html', allproducts=allproducts)

@app.route('/')
def index():
    user = current_user
    if not user.is_authenticated:
        return redirect(url_for('.login'))
    
    return redirect(url_for('.shop'))


@app.route('/signup', methods=['GET', 'POST'])
def signupcliente():
    error = None
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user_ = Usuario.query.filter_by(
                username=request.form['username']).first()
            if user_ is not None:
                error = 'Username ya utilizado'
            else:
                user = Usuario(
                    username=request.form['username'],
                    password=request.form['password'],
                    access=ACCESS['client'],
                    balance=1000
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


@app.route('/login', methods=['GET', 'POST'])
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


def aux_buy_product_list(user, cart):
    bought = []
    fail = []
    for product in cart:
        print(product)
        producto = Producto.query.filter_by(nombre=product.get('name')).first()
        try:
            if producto.stock > product.get('quantity'):
                producto.stock -= product.get('quantity')
                bought.append(producto)
            else:
                fail.append(producto)
        except IntegrityError:
            fail.append(producto)

    if len(bought) > 0:
        compra = Compra(
            user_id=user.id,
            fecha=datetime.now(),
            productos=bought)

        db.session.add(compra)
        db.session.commit()
    else:
        db.session.rollback()

    return bought, fail

def checkifenoughbalance(user, cart):
    bought = []
    fail = []
    totalprice = 0
    for product in cart:
        producto = Producto.query.filter_by(nombre=product.get('name')).first()
        try:
            totalprice = totalprice +  totalprice.precio 
            if totalprice > user.balance:
                bought.append(producto)
            else:
                return 'No hay suficiente saldo en su cuenta'
        except IntegrityError:
            fail.append(producto)
    return ''

@app.route('/buy', methods=['POST'])
def buy_cart():
    user = current_user

    if not is_client(user):
        return redirect(url_for(".index"), code=400)

    cart = request.get_json()
    messagebalance = checkifenoughbalance(user, cart)
    if messagebalance != '':
        obj = {}
        obj['message'] = messagebalance
        return jsonify(obj)

    bought, failed = aux_buy_product_list(user, cart)
    failed_str = ' and '.join((str(product.nombre) for product in failed))
    success, fail = (
        'Bought all products successfully',
        'There were errors while trying to buy: ' + failed_str
    )
    message = success if len(failed) == 0 else fail
    print("message: ",message)
    obj = {}
    obj['message'] = message
    return jsonify(obj)


@app.route('/loginmobile', methods=['POST'])
def loginmobile():
    loginpayload = request.get_json()
    response = {}
    user = Usuario.query.filter_by(username=loginpayload['username']).first()
    message = ""
    if user is None:
        message = 'No existe el usuario'
    else:
        if loginpayload['password'] == user.password:
            message = "Satisfactorio"
            response['username'] = user.username
            response['role'] = user.access
            response['userid'] = user.id
        else:
            message = "Contraseña equivocada"
    response['message'] = message
    return jsonify(response)

@app.route('/products/get-all', methods=['GET'])
def get_all():
    return jsonify([o.to_json() for o in Producto.query.all()])

@app.route('/products/get/<id>', methods=['GET'])
def get_product(id):
    product = Producto.query.filter(Producto.id == id).first()
    if product is None:
        return jsonify({ "found": False })
    return jsonify({ "found": True, "product": product.to_json() })


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
