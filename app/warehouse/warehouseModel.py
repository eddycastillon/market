from app import db
from sqlalchemy.sql import func


class WarehouseModel(db.Model):
    __tablename__ = 'warehouse' # flask migrate
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))
    area = db.Column(db.Integer)
    #
    inventory = db.relationship('InventoryModel', back_populates='warehouse')



    def __repr__(self):
        return f'Warehouse: {self.name}'
