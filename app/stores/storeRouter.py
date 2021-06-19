from app import app
from flask import render_template, request
from flask_login import login_required
from app.stores.storeController import StoreController
from app.stores.storeForm import StoreForm
from app.stores.storeModel import StoreModel


@app.route('/stores')
@login_required
def stores():
    page = request.args.get('page', type=int, default=1)
    controller = StoreController()
    store = controller.records(page)
    return render_template('views/stores/index.html', title='Tiendas', data=store)

@app.route('/stores/create', methods=['GET', 'POST'])
@login_required
def stores_create():
    form = StoreForm()
    if form.validate_on_submit():
        controller = StoreController()
        return controller.create(form)
    return render_template('views/stores/forms/create.html', title='Storees - Crear', form=form)

@app.route('/stores/update/<int:id>', methods=['GET', 'POST'])
@login_required
def stores_update(id):
    store = StoreModel.query.get_or_404(id)
    form = StoreForm(obj=store)
    if form.validate_on_submit():
        controller = StoreController()
        return controller.update(form, id)
    return render_template('views/stores/forms/update.html', 
                        title='Storees - Actualizar', form=form, store_id=store.id)

@app.route('/stores/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def stores_delete(id):
    controller = StoreController()
    return controller.delete(id)
