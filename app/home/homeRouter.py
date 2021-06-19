from app import app
from flask import render_template
from flask_login import login_required
from app.menu.menuController import MenuController


@app.route('/')
@login_required
def index():
    return render_template('views/home/index.html', title='Inicio')


@app.before_request
def before_request():
    controller = MenuController()
    controller.get_all()
