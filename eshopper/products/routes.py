from flask import  render_template, request, session, redirect, url_for,flash,Blueprint
from eshopper import app, db, bcrypt,params
from eshopper.products.modules import product
from eshopper.user.modules import user_login

products = Blueprint('products', __name__)


# for individual item
@products.route("/productname/<string:product11>", methods=['GET'])
def post_route(product11):
    int (product11)
    product1 = product.query.filter_by(productid=product11).first()
    return render_template('product-details.html', product1=product1)


# for sub brand item like samsung/mobilephones
@products.route("/productbrand/<string:brands>/<string:item>", methods=['GET'])
def post_route1(brands,item):
    brandname = product.query.filter_by(brand=brands,categoryname=item).all()

    return render_template('productpage.html', brandname=brandname)


@products.route("/productbrand/<string:brand1>", methods=['GET'])
def post_route2(brand1):

    brandname1 = product.query.filter_by(brand=brand1).all()
    return render_template('productpage.html', brandname1=brandname1)


@products.route("/productcategory/<string:item>", methods=['GET'])
def post_route3(item):

    brandcategory = product.query.filter_by(categoryname=item).all()
    return render_template('productpage.html', brandcategory=brandcategory)


@products.route("/productpage")
def productpage():
    product_pro = product.query.filter_by().all()
    try:
        loginn = user_login.query.filter_by(email=session['user']).first()
        if 'user' in session:
            name=loginn.firstname
    except:
        name=""
    return render_template('productpage.html', product=product_pro)
