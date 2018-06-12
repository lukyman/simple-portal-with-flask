from app import db
from datetime import datetime
from marshmallow import Schema, fields

class FloatUpdate(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    merchant_id = db.Column(db.Integer, db.ForeignKey('merchant.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, merchant_id, amount, created_at, updated_at):
        self.merchant_id = merchant_id
        self.amount = amount
        self.created_at = created_at
        self.updated_at = updated_at

    def __Repr__(self):
        return '<Merchant_float %r>' % self.amount


class FloatBalance(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    merchant_id = db.Column(
        db.Integer, db.ForeignKey('merchant.id'), unique=True)
    amount = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, merchant_id, amount, created_at, updated_at):
        self.merchant_id = merchant_id
        self.amount = amount
        self.created_at = created_at
        self.updated_at = updated_at

    def __Repr__(self):
        return '<Merchant_balance %r>' % self.amount


class FloatConsumption(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    merchant_id = db.Column(
        db.Integer, db.ForeignKey('merchant.id'),  unique=True)
    amount = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)


### Schema ###

class FloatUpdateSchema(Schema):
    id=fields.Int()
    merchant_id = fields.Int()
    amount=fields.Int()
    created_at=fields.DateTime()
    updated_at=fields.DateTime()

class FloatBalanceSchema(Schema):
    id=fields.Int()
    merchant_id = fields.Int()
    amount=fields.Int()
    created_at=fields.DateTime()
    updated_at=fields.DateTime()