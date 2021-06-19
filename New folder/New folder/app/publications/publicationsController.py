from app import db, app
from app.publications.publicationsModel import PublicationsModel
from flask import redirect, url_for, flash
from uuid import uuid4
from werkzeug.utils import secure_filename
from os import path
from sqlalchemy.sql import func
from flask_login import current_user



class PublicationsController:
    def records(self, page):
        return PublicationsModel.query.order_by(PublicationsModel.id).paginate(
            page=page, per_page=5
        )

    def create(self, form, image):
        try:
            # Subida de Imagenes
            random = uuid4().hex[:8]
            image.filename = f'{random}.jpg'
            filename = secure_filename(image.filename)

            destination = path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(destination)
            # End

            publication = PublicationsModel(
                                        title=form.title.data,
                                        content=form.content.data,
                                        image=filename,
                                        category_id=form.category_id.data,
                                        status=1,
                                        date_publish=func.now(),
                                        user_id=current_user.id)
            db.session.add(publication)
            db.session.commit()
            flash('Se creo la publicación con exito !', category='success')
            return redirect(url_for('publications'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('publications_create'))

    def update(self, form, image, publication_id):
        try:
            # Subida de Imagenes
            if image.filename is not None and image.filename != '':
                image.filename = f'{form.image_old}'
                filename = secure_filename(image.filename)

                destination = path.join(app.config['UPLOAD_FOLDER'], filename)
                image.save(destination)
            # End

            publication = PublicationsModel.query.filter_by(id=publication_id).first()
            publication.title = form.title.data
            publication.content = form.content.data
            publication.image = form.image_old
            publication.category_id = form.category_id.data
            publication.user_id = current_user.id
            db.session.commit()
            flash('Se actualizo la publicación con exito !', category='success')
            return redirect(url_for('publications'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('publications_update', id=publication_id))

    def delete(self, publication_id):
        try:
            publication = PublicationsModel.query.filter_by(id=publication_id).first()
            status = 0 if publication.status == 1 else 1
            publication.status = status
            db.session.commit()
            flash('Se cambio el estado con exito !', category='success')
            return redirect(url_for('publications'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrio un error -> {str(e)}', category='danger')
            return redirect(url_for('publications'))
