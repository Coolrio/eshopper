
from eshopper import db


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
    total = db.Column(db.String(25), nullable=True)

