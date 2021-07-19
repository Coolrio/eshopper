from flask import  render_template, request, session, redirect, url_for,flash,Blueprint
from eshopper.products.modules import product
from eshopper.cart1.modules import Cart
from eshopper import app, db, bcrypt,params
from eshopper import home
cart = Blueprint('cart', __name__)


# for individual item
@cart.route("/cart1")
def view_cart():
    if ('user' in session):
        cart1 = Cart.query.filter_by(user=session['user']).all()
        cart2 = Cart.query.filter_by().all()
        total1=0
        for cart2 in cart2:
            total1=total1+cart2.total


        return render_template('cart1.html', cart1=cart1,total1=total1)
    else:
        flash('User is not logged in, Please login before adding items to wishlist', 'danger')
        return redirect(url_for("user.login"))


@cart.route("/cart/<int:product11>")
def add_to_cart(product11):
    if ('user' in session):

        cart_data = product.query.filter_by(productid=product11).first()
        cart1 = Cart(productid=cart_data.productid, user=session['user'], productname=cart_data.productname, productprice=cart_data.productprice, categoryname=cart_data.categoryname, image=cart_data.image, brand=cart_data.brand, stock=cart_data.stock, discount=cart_data.discount, status=cart_data.status, totaltax=cart_data.costaftertax, total=cart_data.total)
        db.session.add(cart1)
        db.session.commit()
    else:
        flash('User is not logged in, Please login before adding items to wishlist', 'danger')
        redirect(url_for("user.login"))
    return redirect(url_for("home.home1"))


@cart.route("/delete/<int:sno>")
def delete_cart_item(sno):
    if ('user' in session):
        delete = Cart.query.filter_by(user=session['user'],sno=sno).first()
        db.session.delete(delete)
        db.session.commit()
    return redirect('/cart1')