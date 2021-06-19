from app import db
from app.products.productModel import ProductModel
from flask import g
from flask import redirect, url_for, flash

class ProductController:
    def records(self, page):
        return ProductModel.query.order_by(ProductModel.id).paginate(
            page=page, per_page=5)

    def create(self, form):
        try:
            product = ProductModel(name=form.name.data, description=form.description.data, code=form.code.data,
                                 stock=form.stock.data, price_base=form.price_base.data, manufacturer=form.manufacturer.data,
                                 type_product=form.type_product.data, expiration_date=form.expiration_date.data)
            db.session.add(product)
            db.session.commit()
            flash(f'Se creo la categoria {form.name.data} con exito !', category='success')
            return redirect(url_for('products'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('products_create'))
    
    def update(self, form, product_id):
        try:
            
            product = ProductModel.query.filter_by(id=product_id).first()
            product.name = form.name.data
            product.description = form.description.data
            product.code = form.code.data
            product.stock = form.stock.data
            product.price_base = form.price_base.data
            product.manufacturer = form.manufacturer.data
            product.type_product = form.type_product.data
            product.expiration_date = form.expiration_date.data
            db.session.commit()
            flash('Se actualizo la categoria con exito !', category='success')
            return redirect(url_for('products'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('products_update', id=product_id))

    def delete(self, product_id):
        try:
            ProductModel.query.filter_by(id=product_id).delete()
            db.session.commit()
            flash('Se cambio el estado con exito !', category='success')
            return redirect(url_for('products'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('products'))

    @staticmethod
    def get_all():
        return ProductModel.query.order_by(ProductModel.name).all()