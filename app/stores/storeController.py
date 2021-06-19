from app import db
from app.stores.storeModel import StoreModel,StoreInventoryModel
from flask import g
from flask import redirect, url_for, flash

class StoreController:
    def records(self, page):
        return StoreModel.query.order_by(StoreModel.id).paginate(
            page=page, per_page=5)

    def create(self, form):
        try:
            store = StoreModel(name=form.name.data, address=form.address.data)
            db.session.add(store)
            db.session.commit()
            flash(f'Se creo la categoria {form.name.data} con exito !', category='success')
            return redirect(url_for('stores'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('stores_create'))
    
    def update(self, form, store_id):
        try:
            
            store = StoreModel.query.filter_by(id=store_id).first()
            store.name = form.name.data
            store.address = form.address.data

            db.session.commit()
            flash('Se actualizo la categoria con exito !', category='success')
            return redirect(url_for('stores'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('stores_update', id=store_id))

    def delete(self, store_id):
        try:
            StoreModel.query.filter_by(id=store_id).delete()
            db.session.commit()
            flash('Se cambio el estado con exito !', category='success')
            return redirect(url_for('stores'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('stores'))

    @staticmethod
    def get_all():
        return StoreInventoryModel.query.all()
        #return StoreInventoryModel.query(StoreInventoryModel.inventory.products.id).all()       