from app import db
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.sql import func

class SaleModel(db.Model):
    __tablename__ = 'sales' # flask migrate
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))

    sale_detail = db.relationship('SaleDetailModel', uselist=False, back_populates='sale') 
    client = db.relationship('ClientModel', uselist=False, back_populates='sale') 
    
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now()) # SELECT NOW()
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
  
    def __repr__(self):
        return f'Sale: {self.name}'

class SaleDetailModel(db.Model):
     __tablename__ = 'sales_details' # flask migrate
     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
     sale_id = db.Column(db.Integer, db.ForeignKey('sales.id'))
     product_id = db.Column(db.Integer, db.ForeignKey('store_inventory.id'))
     #
     sale = db.relationship('SaleModel', uselist=False, back_populates='sale_detail') 
     product = db.relationship('StoreInventoryModel', uselist=False, back_populates='sale_detail') 
     

     created_at = db.Column(db.DateTime(timezone=True), server_default=func.now()) # SELECT NOW()
     updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
  