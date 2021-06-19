from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, IntegerField, FloatField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired('Este campo es requerido')])
    description = TextAreaField('Descripción', validators=[DataRequired('Este campo es requerido')])
    code = StringField('Código interno', validators=[DataRequired('Este campo es requerido')])
    stock = IntegerField('Cantidad', validators=[DataRequired('Este campo es requerido')])
    price_base = FloatField('Precio base', validators=[DataRequired('Este campo es requerido')])
    manufacturer = StringField('Proveedor', validators=[DataRequired('Este campo es requerido')])
    type_product = StringField('Tipo de producto', validators=[DataRequired('Este campo es requerido')])
    expiration_date = DateField('Fecha de vencimiento', format='%m/%d/%Y', validators=[DataRequired('Este campo es requerido')])
    submit = SubmitField('Enviar')
