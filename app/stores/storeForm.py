from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class StoreForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired('Este campo es requerido')])
    address = StringField('Dirección', validators=[DataRequired('Este campo es requerido')])
    submit = SubmitField('Enviar')
