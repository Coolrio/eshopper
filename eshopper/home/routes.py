from flask import Flask, render_template, request, session, redirect, url_for,flash,Blueprint
from eshopper import app, db, bcrypt,mail,c,params
from eshopper.user.modules import user_login
from eshopper.products.modules import product

home = Blueprint('home', __name__)

@home.route("/")
@home.route("/home")
def home1():

    product_pro = product.query.filter_by().all()[0:6]
    brand=product.query.filter_by(brand="samsung").all()[0:6]
    wired_earphone = product.query.filter_by(categoryname="wired_earphone").all()[0:6]
    laptop=product.query.filter_by(categoryname="laptop").all()[0:6]
    mobile = product.query.filter_by(categoryname="mobilephones").all()[0:6]
    tv = product.query.filter_by(categoryname="tv").all()[0:6]
    washing = product.query.filter_by(categoryname="washingmachine").all()[0:6]
    try:
        loginn = user_login.query.filter_by(email=session['user']).first()
        if 'user' in session:
            name=loginn.firstname
    except:
        name=""

    return render_template('index.html', product=product_pro, brand=brand, mobile=mobile, wired_earphone=wired_earphone
                           ,laptop=laptop,washing=washing,tv=tv,name=name)


@home.route("/search", methods=['GET'])
def searchbar():

       # brandname = product.query.filter_by(brand=serach_string).all()
        return render_template('productpage.html')