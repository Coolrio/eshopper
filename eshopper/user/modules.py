from datetime import datetime
from eshopper import db



class user_login(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(15), nullable=False)
    lastname = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(25), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    dob = db.Column(db.String(25), nullable=False)
    address = db.Column(db.String(60), nullable=False)
    pincode = db.Column(db.String(6), nullable=False)
    city = db.Column(db.String(15), nullable=False)
    landmark = db.Column(db.String(25), nullable=False)
    houseno = db.Column(db.String(10), nullable=False)
    state = db.Column(db.String(25), nullable=False)
    country = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(15), nullable=True)



