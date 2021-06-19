from app import app
from flask import render_template, request
from flask_login import login_required
from app.inventories.inventoryController import InventoryController
from app.products.productController import ProductController
from app.warehouse.warehouseController import WarehouseController
from app.inventories.inventoryForm import InventoryForm
from app.inventories.inventoryModel import InventoryModel


@app.route('/inventories')
@login_required
def inventories():
    page = request.args.get('page', type=int, default=1)
    controller = InventoryController()
    inventory = controller.records(page)
    return render_template('views/inventories/index.html', title='Inventario', data=inventory)

@app.route('/inventories/create', methods=['GET', 'POST'])
@login_required
def inventories_create():
    form = InventoryForm()
    # Get Products
    products = ProductController.get_all() # [(id, nombre)]
    warehouses = WarehouseController.get_all()
    form.product_id.choices = [(c.id, c.name) for c in products]
    form.warehouse_id.choices = [(c.id, c.name) for c in warehouses]
    if form.validate_on_submit():
        controller = InventoryController()
        return controller.create(form)
    return render_template('views/inventories/forms/create.html', title='Inventario - Crear', form=form)

@app.route('/inventories/update/<int:id>', methods=['GET', 'POST'])
@login_required
def inventories_update(id):
    inventory = InventoryModel.query.get_or_404(id)
    form = InventoryForm(obj=inventory)
    # Get Products
    products = ProductController.get_all() # [(id, nombre)]
    warehouses = WarehouseController.get_all()
    form.product_id.choices = [(c.id, c.name) for c in products]
    form.warehouse_id.choices = [(c.id, c.name) for c in warehouses]
    if form.validate_on_submit():
        controller = InventoryController()
        return controller.update(form, id)
    return render_template('views/inventories/forms/update.html', 
                        title='Inventario - Actualizar', form=form, inventory_id=inventory.id)

@app.route('/inventories/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def inventories_delete(id):
    controller = InventoryController()
    return controller.delete(id)
