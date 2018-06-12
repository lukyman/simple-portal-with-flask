from app import db
from datetime import datetime
from marshmallow import Schema, fields


class PortalUser(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, fullname, username, email, password, active, created_at, updated_at):
        self.fullname = fullname
        self.username = username
        self.email = email
        self.password = password
        self.active = active
        self.created_at = created_at
        self.updated_at = updated_at
