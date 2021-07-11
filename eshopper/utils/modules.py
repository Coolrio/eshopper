from datetime import datetime
from eshopper import db




class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(500), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(50), nullable=False)

