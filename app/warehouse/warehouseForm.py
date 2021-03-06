from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class WarehouseForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired('Este campo es requerido')])
    location = StringField('Ubicacion', validators=[DataRequired('Este campo es requerido')])
    area = StringField('Area', validators=[DataRequired('Este campo es requerido')])
    submit = SubmitField('Enviar')
