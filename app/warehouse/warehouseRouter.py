from app import app
from flask import render_template, request
from flask_login import login_required
from app.warehouse.warehouseForm import  WarehouseForm
from app.warehouse.warehouseController import WarehouseController
from app.warehouse.warehouseModel import WarehouseModel


@app.route('/warehouse')
@login_required
def warehouse():
    page = request.args.get('page', type=int, default=1)
    controller = WarehouseController()
    warehouse = controller.records(page)
    return render_template('views/warehouse/index.html', title='Almacenes', data=warehouse)

@app.route('/warehouse/create', methods=['GET', 'POST'])
@login_required
def warehouse_create():
    form = WarehouseForm()
    if form.validate_on_submit():
        controller = WarehouseController()
        return controller.create(form)
    return render_template('views/warehouse/forms/create.html', title='Almacenes - Crear', form=form)

@app.route('/warehouse/update/<int:id>', methods=['GET', 'POST'])
@login_required
def warehouse_update(id):
    warehouse = WarehouseModel.query.get_or_404(id)
    form = WarehouseForm(obj=warehouse)
    if form.validate_on_submit():
        controller = WarehouseController()
        return controller.update(form, id)
    return render_template('views/warehouse/forms/update.html', 
                        title='Almacen - Actualizar', form=form, warehouse_id=warehouse.id)

@app.route('/warehouse/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def warehouse_delete(id):
    controller = WarehouseController()
    return controller.delete(id)

