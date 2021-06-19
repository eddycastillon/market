from app import db
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.sql import func

class StoreModel(db.Model):
    __tablename__ = 'stores' # flask migrate
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(100))
    # 
    store_inventory = db.relationship('StoreInventoryModel', uselist=False, back_populates='store') 

    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now()) # SELECT NOW()
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
  
    def __repr__(self):
        return f'Store: {self.name}'

class StoreInventoryModel(db.Model):
    __tablename__ = 'store_inventory'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventories.id'))
    #
    store = db.relationship('StoreModel', uselist=False, back_populates='store_inventory')
    inventory = db.relationship('InventoryModel', uselist=False, back_populates='store_inventory', lazy="joined", join_depth=2)
    sale_detail = db.relationship('SaleDetailModel', uselist=False, back_populates='product') 

    def __repr__(self):
     return f'StoreInventory: {self.inventory.products}'