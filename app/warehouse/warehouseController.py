from app import db
from app.warehouse.warehouseModel import WarehouseModel
from flask import g
from flask import redirect, url_for, flash

class WarehouseController:

    def records(self, page):
        return WarehouseModel.query.order_by(WarehouseModel.id).paginate(
            page=page, per_page=5
        )

    def create(self, form):
        try:
            warehouse = WarehouseModel(name=form.name.data, location=form.location.data, area=form.area.data)
            db.session.add(warehouse)
            db.session.commit()
            flash(f'Se creo la categoria {form.name.data} con exito !', category='success')
            return redirect(url_for('warehouse'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('warehouse_create'))
    
    def update(self, form, warehouse_id):
        try:
            warehouse = WarehouseModel.query.filter_by(id=warehouse_id).first()
            warehouse.name = form.name.data
            warehouse.location = form.location.data
            warehouse.area = form.area.data
            db.session.commit()
            flash('Se actualizo la categoria con exito !', category='success')
            return redirect(url_for('warehouse'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('warehouse_update', id=warehouse_id))

    def delete(self, warehouse_id):
        try:
            WarehouseModel.query.filter_by(id=warehouse_id).delete()
            db.session.commit()
            flash('Se cambio el estado con exito !', category='success')
            return redirect(url_for('warehouse'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('warehouse'))

    @staticmethod
    def get_all():
        return WarehouseModel.query.order_by(WarehouseModel.name).all()