from app import db
from app.sales.saleModel import SaleModel
from flask import g
from flask import redirect, url_for, flash

class SaleController:
    def records(self, page):
        return SaleModel.query.order_by(SaleModel.id).paginate(
            page=page, per_page=5)

    def create(self, form):
        try:
            sale = SaleModel(client_id=form.client_id.data)
            db.session.add(sale)
            db.session.commit()
            flash(f'Registro guardado con exito !', category='success')
            return redirect(url_for('sales_update', id=sale.id))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('sales_create'))
    
    def update(self, form, sale_id):
        try:
            
            sale = SaleModel.query.filter_by(id=sale_id).first()
            sale.name = form.name.data
            sale.address = form.address.data

            db.session.commit()
            flash('Se actualizo la categoria con exito !', category='success')
            return redirect(url_for('sales'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('sales_update', id=sale_id))

    def delete(self, sale_id):
        try:
            SaleModel.query.filter_by(id=sale_id).delete()
            db.session.commit()
            flash('Se cambio el estado con exito !', category='success')
            return redirect(url_for('sales'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('sales'))