from app import db
from app.inventories.inventoryModel import InventoryModel
from flask import g
from flask import redirect, url_for, flash

class InventoryController:
    def records(self, page):
        return InventoryModel.query.order_by(InventoryModel.id).paginate(
            page=page, per_page=5)

    def create(self, form):
        try:
            inventory = InventoryModel(stock=form.stock.data, product_id=form.product_id.data,
                                     warehouse_id=form.warehouse_id.data )
            db.session.add(inventory)
            db.session.commit()
            flash(f'Registro guardado con exito !', category='success')
            return redirect(url_for('inventories'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('inventories_create'))
    
    def update(self, form, inventory_id):
        try:
            
            inventory = InventoryModel.query.filter_by(id=inventory_id).first()
            inventory.stock = form.stock.data
            inventory.warehouse_id = form.warehouse_id.data
            inventory.product_id = form.product_id.data

            db.session.commit()
            flash(f'Registro actualizado con exito !', category='success')
            return redirect(url_for('inventories'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('inventories_update', id=inventory_id))

    def delete(self, inventory_id):
        try:
            InventoryModel.query.filter_by(id=inventory_id).delete()
            db.session.commit()
            flash('Se cambio el estado con exito !', category='success')
            return redirect(url_for('inventories'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('inventories'))