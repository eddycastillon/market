from app import app
from flask import render_template, request
from flask_login import login_required
from app.sales.saleController import SaleController
from app.stores.storeController import StoreController
from app.clients.clientController import ClientController
from app.sales.saleForm import SaleForm, SaleProductForm
from app.sales.saleModel import SaleModel


@app.route('/sales')
@login_required
def sales():
    page = request.args.get('page', type=int, default=1)
    controller = SaleController()
    sale = controller.records(page)
    return render_template('views/sales/index.html', title='Ventas', data=sale)

@app.route('/sales/create', methods=['GET', 'POST'])
@login_required
def sales_create():
    form = SaleForm()
    clients = ClientController.get_all()
    form.client_id.choices = [(c.id, c.name) for c in clients]
    if form.validate_on_submit():
        controller = SaleController()
        return controller.create(form)
    return render_template('views/sales/forms/create.html', title='Salees - Crear', form=form)

@app.route('/sales/update/<int:id>', methods=['GET', 'POST'])
@login_required
def sales_update(id):
    sale = SaleModel.query.get_or_404(id)
    form = SaleForm(obj=sale)
    clients = ClientController.get_all()
    form.client_id.choices = [(c.id, c.name) for c in clients]
    if form.validate_on_submit():
        controller = SaleController()
        return controller.update(form, id)
    return render_template('views/sales/forms/update.html', 
                        title='Salees - Actualizar', form=form, sale_id=sale.id)

@app.route('/sales/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def sales_delete(id):
    controller = SaleController()
    return controller.delete(id)

@app.route('/sales/product')
@login_required
def sales_add_product():
    #form = SaleProductForm()
    products = StoreController.get_all()
    print(products)
    #form.product_id.choices = [(c.id, c.inventory_id) for c in products]
 
    return render_template('views/sales/forms/add_product.html', title='Salees - Crear', form=products)