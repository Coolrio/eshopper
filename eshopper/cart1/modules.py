
from eshopper import db


class Cart(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    productid = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(25), nullable=False)
    productname = db.Column(db.String(50), nullable=False)
    productprice = db.Column(db.String(25), nullable=False)
    categoryname= db.Column(db.String(25), nullable=True)
    image = db.Column(db.String(50), nullable=False)
    brand = db.Column(db.String(12), nullable=True)
    stock = db.Column(db.String(25), nullable=True)
    discount = db.Column(db.String(25), nullable=False)
    totaltax = db.Column(db.String(25), nullable=False)
    total = db.Column(db.Float(25), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    categoryname= db.Column(db.String(25), nullable=True)

