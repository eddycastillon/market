from app import db

class ClientModel(db.Model):
    __tablename__ = 'client' # flask migrate
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    identity_document = db.Column(db.Integer)
    email = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    address = db.Column(db.String(50))
    
    sale = db.relationship('SaleModel', uselist=False, back_populates='client') 


    def __repr__(self):
        return f'Client: {self.name}'
