from app import app
from flask import render_template, request
from flask_login import login_required
from app.clients.clientController import ClientController
from app.clients.clientForm import ClientForm
from app.clients.clientModel import ClientModel


@app.route('/clients')
@login_required
def clients():
    page = request.args.get('page', type=int, default=1)
    controller = ClientController()
    client = controller.records(page)
    return render_template('views/clients/index.html', title='Clientes', data=client)

@app.route('/clients/create', methods=['GET', 'POST'])
@login_required
def clients_create():
    form = ClientForm()
    if form.validate_on_submit():
        controller = ClientController()
        return controller.create(form)
    return render_template('views/clients/forms/create.html', title='Clientes - Crear', form=form)

@app.route('/clients/update/<int:id>', methods=['GET', 'POST'])
@login_required
def clients_update(id):
    client = ClientModel.query.get_or_404(id)
    form = ClientForm(obj=client)
    if form.validate_on_submit():
        controller = ClientController()
        return controller.update(form, id)
    return render_template('views/clients/forms/update.html', 
                        title='Clientes - Actualizar', form=form, client_id=client.id)

@app.route('/clients/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def clients_delete(id):
    controller = ClientController()
    return controller.delete(id)
