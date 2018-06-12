from app import db
from datetime import datetime
from float import FloatUpdate

class Merchant(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    business_name = db.Column(db.String(120), nullable=False)
    registration_number = db.Column(db.String(100), nullable=True)
    date_of_reg = db.Column(db.DateTime, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    physical_address = db.Column(db.String(150), nullable=False)
    box_number = db.Column(db.String(100), nullable=True)
    code = db.Column(db.String(8), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    merchant = db.relationship('FloatUpdate', backref='merchant', cascade='all, delete-orphan', lazy=True)
    
    def __init__(self, business_name, registration_number, date_of_reg, email, physical_address, box_number, code):
        self.business_name = business_name
        self.registration_number = registration_number
        self.date_of_reg = date_of_reg
        self.email = email
        self.physical_address = physical_address,
        self.box_number = box_number
        self.code = code

    def __repr__(self):
        return '<Merchant %r>' % self.business_name
