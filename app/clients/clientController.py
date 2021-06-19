from app import db
from app.clients.clientModel import ClientModel
from flask import g
from flask import redirect, url_for, flash

class ClientController:
    def records(self, page):
        return ClientModel.query.order_by(ClientModel.id).paginate(
            page=page, per_page=5
        )
    def create(self, form):
        try:
            client = ClientModel(name=form.name.data, lastname=form.lastname.data, identity_document=form.identity_document.data,
                                 email=form.email.data, phone=form.phone.data, address=form.address.data)
            db.session.add(client)
            db.session.commit()
            flash(f'Se creo la categoria {form.name.data} con exito !', category='success')
            return redirect(url_for('clients'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('clients_create'))
    
    def update(self, form, client_id):
        try:
            
            client = ClientModel.query.filter_by(id=client_id).first()
            client.name = form.name.data
            client.lastname = form.lastname.data
            client.identity_address = form.identity_document.data
            client.email = form.email.data
            client.phone = form.phone.data
            client.address = form.address.data
            db.session.commit()
            flash('Se actualizo la categoria con exito !', category='success')
            return redirect(url_for('clients'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('clients_update', id=client_id))

    def delete(self, client_id):
        try:
            ClientModel.query.filter_by(id=client_id).delete()
            db.session.commit()
            flash('Se cambio el estado con exito !', category='success')
            return redirect(url_for('clients'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('clients'))

    @staticmethod
    def get_all():
        return ClientModel.query.order_by(ClientModel.name).all()