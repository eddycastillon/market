from app import db


class CategoriesModel(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), index=True)
    status = db.Column(db.Integer)

    def __repr__(self):
        return f'Category: {self.name}'
