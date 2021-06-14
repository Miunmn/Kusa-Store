from database import connector
from model import entities

from flask import Flask, flash, request, redirect, url_for, render_template, session, Response
import os
import urllib.request
from werkzeug.utils import secure_filename

from flask_login import login_required, current_user, login_user, logout_user
from flask_login import LoginManager


import json
import time
from datetime import datetime

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__,
    static_folder='',
    static_url_path='/static'
)

user_session_key='user'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

IMAGENES_PRODUCTOS_FOLDER = 'static/images/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['IMAGENES_PRODUCTOS_FOLDER'] = IMAGENES_PRODUCTOS_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == str(user_id)).first()

#landing-page view
@app.route('/', methods = ['GET'])
def get_index():
    return render_template('index.html')

@app.route('/eliminarproducto')
def eliminarproducto():
    return render_template('eliminar.html')

#catalogo
@app.route('/catalogo')
def vercatalogo():
    return render_template('catalogo.html')

@app.route('/login', methods=['GET','POST'])
def loginadministrator():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        db_session = db.getSession(engine)
        respuesta = db_session.query(entities.User).filter(entities.User.username == user).filter(entities.User.password == password)
        db_session.close()
        if len(respuesta)>0:
            login_user(respuesta[0])
            flash('logged in')
            print("LOGEADO")
        return render_template('catalogo.html')
    return render_template('login.html')

###
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/add_product')
def upload_form():
    return render_template('agregado.html')
 #   return redirect('static2/agregado.html')
	
@app.route('/add_product', methods=['POST'])
def upload_image():
	if 'files[]' not in request.files:
		flash('No file part')
		return redirect(request.url)
	files = request.files.getlist('files[]')
	file_names = []
	for file in files:
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file_names.append(filename)
			file.save(os.path.join(app.config['IMAGENES_PRODUCTOS_FOLDER'], filename))
		#else:
		#	flash('Allowed image types are -> png, jpg, jpeg, gif')
		#	return redirect(request.url)
	return render_template('agregado.html', filenames=file_names)
###
'''    db_session = db.getSession(engine)
    rq_msg = json.loads(request.data)
    username = rq_msg
    respuesta = db_session.query(entities.User).filter(entities.User.username == rq_msg['username']).filter(entities.User.password == rq_msg['password'])
    db_session.close()
    users = respuesta[:]
    if len(users) != 0:
        session['user'] = json.dumps(users[0], cls=connector.AlchemyEncoder);
        r_msg = {'msg':'Welcome!', 'id': users[0].id, 'username': users[0].username}
        json_msg = json.dumps(r_msg, cls=connector.AlchemyEncoder)
        return Response(json_msg, status=200, mimetype='application/json')
    r_msg = {'msg':'Failed'}
    json_msg = json.dumps(r_msg, cls=connector.AlchemyEncoder)
    return Response(json_msg, status=401, mimetype='application/json')'''

'''@app.route('/login', methods=['POST'])
def login():
    print(request.form.get('username'))
    key = 'username'
    username = request.form.get('username')
    password = request.form.get('password')
    db_session = db.getSession(engine)
    respuesta = db_session.query(entities.User).filter(entities.User.username == username).filter(entities.User.password == password)
    db_session.close()
    users = respuesta[:]
    if len(users)> 0:
        session[key] = json.dumps(users[0], cls =connector.AlchemyEncoder)
        print(session[key])
        return redirect("static/html/chat.html")
    return redirect('static/html/login.html')'''
'''    if user_session_key in session:
        session.pop(user_session_key)
    response = {'msg':'Logged out'}
    json_response = json.dumps(response)
'''
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out.')
    print('You were logged out.')
    return render_template('login.html')

@app.route('/signup', methods=['POST'])
def signup():
    user = json.loads(request.data)
    email = user['email']
    username = user['username']
    name = user['name']
    fullname = user['fullname']
    password = user['password']
    
    new_user = entities.User(email=email, username=username, name=name, fullname=fullname, password=password)

    #user_session_key = 'user'

    session = db.getSession(engine)
    session.add(new_user)
    session.commit()
    session.close()
    rpta_msg = {'msg':'Register success'}
    json_rpta_msg = json.dumps(rpta_msg, cls=connector.AlchemyEncoder)
    return Response(json_rpta_msg, status=201, mimetype='application/json')


#CRUD users
@app.route('/users', methods = ['POST'])
def create_user():
    #c = json.loads(request.data)
    c = json.loads(request.form['values'])
    user = entities.User(
        email=c['email'],
        username=c['username'],
        name=c['name'],
        fullname=c['fullname'],
        password=c['password']
    )
    session = db.getSession(engine)
    session.add(user)
    session.commit()
    session.close()
    r_msg = {'msg':'UserCreated'}
    json_msg = json.dumps(r_msg, cls=connector.AlchemyEncoder)
    return Response(json_msg, status=201, mimetype='application/json')

@app.route('/users/<id>', methods = ['GET'])
def get_user(id):
    db_session = db.getSession(engine)
    users = db_session.query(entities.User).filter(entities.User.id == id)
    db_session.close()
    for user in users:
        js = json.dumps(user, cls=connector.AlchemyEncoder)
        return  Response(js, status=200, mimetype='application/json')
    message = { 'status': 404, 'message': 'Not Found'}
    return Response(json.dumps(message), status=404, mimetype='application/json')

key_users = 'users'
cache = {}

@app.route('/users', methods = ['GET'])
def get_users():
    data = []

    if key_users in cache and (datetime.now() - cache[key_users]['time']).total_seconds() < 20:
        # Get cache
        data = cache[key_users]['data']
    else:
        session = db.getSession(engine)
        dbResponse = session.query(entities.User).order_by(entities.User.username)
        session.close()
        data = dbResponse[:]
        # Set cache
        cache[key_users] = {'data': data, 'time': datetime.now()}
    
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

@app.route('/users', methods = ['PUT'])
def update_user():
    session = db.getSession(engine)
    id = request.form['key']
    user = session.query(entities.User).filter(entities.User.id == id).first()
    c = json.loads(request.form['values'])

    for key in c.keys():
        setattr(user, key, c[key])

    session.add(user)
    session.commit()
    session.close()
    return 'Updated User'

@app.route('/users', methods = ['DELETE'])
def delete_user():
    id = request.form['key']
    session = db.getSession(engine)
    user = session.query(entities.User).filter(entities.User.id == id).one()
    session.delete(user)
    session.commit()
    session.close()
    return "Deleted User"


@app.route('/current')
def current():
    user_json = session['user']
    return Response(user_json, status=200, mimetype="application/json")

@app.route('/create', methods=['POST'])
def create():
    producto = json.loads(request.data)
    categoria = producto['categoria']
    nombre = producto['nombre']
    descripcion = producto['descripcion']
    precio = producto['precio']
    
    new_producto = entities.Producto(categoria=categoria, nombre=nombre, descripcion=descripcion, precio=precio)

    session = db.getSession(engine)
    session.add(new_producto)
    session.commit()
    rpta_msg = {'msg':'Producto_Created'}
    json_rpta_msg = json.dumps(rpta_msg, cls=connector.AlchemyEncoder)
    return Response(json_rpta_msg, status=201, mimetype='application/json')





#CRUD productos
@app.route('/productos', methods = ['POST'])
def create_producto():
    #c = json.loads(request.data)
    c = json.loads(request.form['values'])
    producto = entities.Producto(
        categoria=c['categoria'],
        nombre=c['nombre'],
        descripcion=c['descripcion'],
        precio=c['precio']
        #vista=c['vista']
       
    )
    session = db.getSession(engine)
    session.add(producto)
    session.commit()
    r_msg = {'msg':'Producto_Created'}
    json_msg = json.dumps(r_msg, cls=connector.AlchemyEncoder)
    return Response(json_msg, status=201,mimetype='application/json')

@app.route('/productos/<id>', methods = ['GET'])
def get_producto(id):
    db_session = db.getSession(engine)
    productos = db_session.query(entities.Producto).filter(entities.Producto.id == id)
    for producto in productos:
        js = json.dumps(producto, cls=connector.AlchemyEncoder)
        return  Response(js, status=200, mimetype='application/json')
    message = { 'status': 404, 'message': 'Not Found'}
    return Response(json.dumps(message), status=404, mimetype='application/json')

@app.route('/productos', methods = ['GET'])
def get_productos():
    session = db.getSession(engine)
    dbResponse = session.query(entities.Producto)
    data = dbResponse[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

@app.route('/productos', methods = ['PUT'])
def update_producto():
    session = db.getSession(engine)
    id = request.form['key']
    producto = session.query(entities.Producto).filter(entities.Producto.id == id).first()
    c = json.loads(request.form['values'])

    for key in c.keys():
        setattr(producto, key, c[key])

    session.add(producto)
    session.commit()
    return 'Updated Producto'



@app.route('/productos/nombre', methods = ['DELETE'])
def delete_producto(nombre):
    session = db.getSession(engine)
    producto = session.query(entities.Producto).filter(entities.Producto.nombre == nombre).one()
    session.delete(producto)
    session.commit()
    return "Deleted Producto"








@app.route('/frutasyverduras', methods=['GET'])
def frutasyverduras():
    session = db.getSession(engine)
    dbResponse = session.query(entities.Producto).filter(entities.Producto.categoria=="Frutasyverduras")
    data = dbResponse[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

@app.route('/bebidas', methods=['GET'])
def bebidas():
    session = db.getSession(engine)
    dbResponse = session.query(entities.Producto).filter(entities.Producto.categoria=="Bebidas")
    data = dbResponse[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

@app.route('/carnes', methods=['GET'])
def carnes():
    session = db.getSession(engine)
    dbResponse = session.query(entities.Producto).filter(entities.Producto.categoria=="Carnes-Ave-Pescado")
    data = dbResponse[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

@app.route('/limpieza', methods=['GET'])
def limpieza():
    session = db.getSession(engine)
    dbResponse = session.query(entities.Producto).filter(entities.Producto.categoria=="Limpieza")
    data = dbResponse[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

if __name__ == '__main__':
    app.secret_key = "FM8uh@#94$!#@we!@#!$3342$#@$#@DWQCSA$23"
    app.run(port=8081, threaded=True, host=('127.0.0.1'))
