from app import db
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.sql import func

class InventoryModel(db.Model):
    __tablename__ = 'inventories' # flask migrate
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stock = db.Column(db.Integer)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    warehouse_id = db.Column(db.Integer, db.ForeignKey('warehouse.id'))
    #
    warehouse = db.relationship('WarehouseModel', uselist=False, back_populates='inventory')
    products = db.relationship('ProductModel', uselist=False, back_populates='inventory')
    store_inventory = db.relationship('StoreInventoryModel', uselist=False, back_populates='inventory', lazy="joined", join_depth=2)
     
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now()) # SELECT NOW()
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())


  
    def __repr__(self):
        return f'Inventory: {self.id}'
