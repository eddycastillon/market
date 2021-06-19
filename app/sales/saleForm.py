from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class SaleForm(FlaskForm):
    client_id = SelectField('Cliente', coerce=int, 
                    validators=[DataRequired('Este campo es necesario')])    
    submit = SubmitField('Enviar')

class SaleProductForm(FlaskForm):
    product_id = SelectField('Producto', coerce=int, 
                    validators=[DataRequired('Este campo es necesario')])    
    submit = SubmitField('Enviar')