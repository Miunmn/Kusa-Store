from sqlalchemy.sql.sqltypes import Integer
from flask_wtf import FlaskForm
from werkzeug.datastructures import Range
from wtforms import StringField, PasswordField, FloatField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo


class RegisterForm(FlaskForm):
    pass
    #name = StringField('Name',validators=[DataRequired(), Length(min=3, max=25)])
    #username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    #password = PasswordField('Password',validators=[DataRequired(), Length(min=10, max=25)])


class ProductForm(FlaskForm):
    pass
    #nombre = StringField('nombre', validators=[DataRequired(), Length(min=5, max=40)])
    #descripcion = StringField('descripcion', validators=[DataRequired(), Length(min=3, max=25)])
    #url = [DataRequired(), URL(message='Must be a valid URL')]validators=[DataRequired(), Range(3.0,25.0)] )

    #precio = FloatField('precio',

class CreateProductForm(FlaskForm):
    nombre = StringField('nombre', validators=[DataRequired(), Length(min=3, max=255)])
    descripcion = StringField('descripcion', validators=[DataRequired(), Length(min=3, max=255)])
    precio = FloatField('precio', validators=[DataRequired(), Length(min=3, max=255)])
    stock = IntegerField('stock', validators=[DataRequired(), Length(min=3, max=255)])
    img_url = StringField('img_url', validators=[DataRequired(), Length(min=3, max=255)])