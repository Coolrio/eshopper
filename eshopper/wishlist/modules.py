
from eshopper import db


class Wishlist(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    productid = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(25), nullable=False)
    productname = db.Column(db.String(50), nullable=False)
    productprice = db.Column(db.String(25), nullable=False)
    categoryname= db.Column(db.String(25), nullable=True)
    image = db.Column(db.String(25), nullable=False)
    brand = db.Column(db.String(12), nullable=True)



