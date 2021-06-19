from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ClientForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired('Este campo es requerido')])
    lastname = StringField('Apellidos', validators=[DataRequired('Este campo es requerido')])
    identity_document = StringField('Nro Documento', validators=[DataRequired('Este campo es requerido')])
    email = StringField('Email', validators=[DataRequired('Este campo es requerido')])
    phone = StringField('Celular', validators=[DataRequired('Este campo es requerido')])
    address = StringField('Dirección', validators=[DataRequired('Este campo es requerido')])
    submit = SubmitField('Enviar')
