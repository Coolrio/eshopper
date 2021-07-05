from datetime import datetime
from eshopper import db




class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(500), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(50), nullable=False)


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

class product(db.Model):
    productid = db.Column(db.Integer, primary_key=True)
    productname = db.Column(db.String(25), nullable=False)
    productprice = db.Column(db.String(25), nullable=False)
    categoryname= db.Column(db.String(25), nullable=True)
    categoryid = db.Column(db.String(25), nullable=False)
    title = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    costbeforetax = db.Column(db.String(25), nullable=False)
    gst = db.Column(db.String(10), nullable=False)
    discount = db.Column(db.String(25), nullable=False)
    quantity = db.Column(db.String(25), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    subcategoryid = db.Column(db.String(25), nullable=False)
    costaftertax = db.Column(db.String(10), nullable=False)
    image = db.Column(db.String(25), nullable=False)
    soldby = db.Column(db.String(15), nullable=True)
    brand = db.Column(db.String(12), nullable=True)
    stock = db.Column(db.String(25), nullable=True)


