from app import db
from datetime import datetime

class MerchantCode(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(8), unique= True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, code, created_at, updated_at):
        self.code = code
        self.created_at = created_at
        self.updated_at = updated_at