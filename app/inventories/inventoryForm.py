from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired


class InventoryForm(FlaskForm):
    stock = IntegerField('Cantidad', validators=[DataRequired('Este campo es requerido')])
    product_id = SelectField('Producto', coerce=int, 
                    validators=[DataRequired('Este campo es necesario')])
    warehouse_id = SelectField('Almacen', coerce=int, 
                    validators=[DataRequired('Este campo es necesario')])
    submit = SubmitField('Enviar')
