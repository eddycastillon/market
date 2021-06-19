from app import db
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.sql import func

class ProductModel(db.Model):
    __tablename__ = 'products' # flask migrate
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    code = db.Column(db.String(100))
    stock = db.Column(db.Integer)
    price_base = db.Column(db.Float)
    manufacturer = db.Column(db.String(100)) # Move to other table
    type_product = db.Column(db.String(100)) # Move to other table
    expiration_date = db.Column(db.DateTime(timezone=True))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now()) # SELECT NOW()
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    #
    inventory = db.relationship('InventoryModel', back_populates='products')


  
    def __repr__(self):
        return f'Product: {self.name}'
