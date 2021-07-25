from flask import  render_template, request, session, redirect, url_for,flash,Blueprint
from eshopper import app, db, bcrypt,params
from eshopper.products.modules import product
from eshopper.user.modules import user_login
from eshopper.home.routes import searchbar
import math
from eshopper.wishlist.modules import Wishlist
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
    page = request.args.get('page', 1, type=int)
    brandname = product.query.filter_by(brand=brands,categoryname=item).paginate(page=page, per_page=6)
    return render_template('productpage-probrand.html', brandname=brandname)


@products.route("/productbrand/<string:item>", methods=['GET'])
def post_route2(item):
    page = request.args.get('page', 1, type=int)
    brandname1 = product.query.filter_by(brand=item).paginate(page=page, per_page=6)
    return render_template('productpage-brand1.html', brandname1=brandname1,item=item)


@products.route("/page")
def page():
    products = product.query.filter_by().all()
    last = math.ceil(len(products) / int(params['no_of_posts']))
    # posts=posts()
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
        page = int(page)
    products = products[(page - 1) * int(params['no_of_posts']): (page - 1) * int(params['no_of_posts']) + int(params['no_of_posts'])]

    if page == 1:
        prev = "#"
        next = "/?page=" + str(page + 1)
    elif page == last:
        prev = "/?page=" + str(page - 1)
        next = "#"
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)
    return render_template('productpage.html', params=params, products=products, prev=prev, next=next)


@products.route("/searchbar", methods=['GET'])
def post_route4():
    search=searchbar.serach_string
    brandname2 = product.query.filter_by(brand=search).all()
    return render_template('productpage.html', brandname2=brandname2)


@products.route("/productcategory/<string:item>", methods=['GET'])
def post_route3(item):
    if request.method == 'GET':
        if request.form['submit_button'] == 'Do Something':
            pass  # do something
        elif request.form['submit_button'] == 'Do Something Else':
            pass  # do something else
        else:
            pass  # unknown
    page = request.args.get('page', 1, type=int)
    brandcategory = product.query.filter_by(categoryname=item).paginate(page=page, per_page=2)
    return render_template('productpage-category.html', brandcategory=brandcategory,item=item)


@products.route("/productpage")
def productpage():
    page = request.args.get('page', 1, type=int)
    product_pro = product.query.filter_by().paginate(page=page, per_page=5)
    try:
        loginn = user_login.query.filter_by(email=session['user']).first()
        if 'user' in session:
            name=loginn.firstname
    except:
        name=""
    return render_template('productpage.html', product=product_pro)


# for individual item
@products.route("/wishlist/<string:product11>", methods=['GET'])
def wishlist(product11):
    int (product11)
    page = request.args.get('page', 1, type=int)
    product1 = product.query.filter_by(productid=product11).first()
    return render_template('product-details.html', product1=product1)