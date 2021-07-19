from flask import  render_template, request, session, redirect, url_for,flash,Blueprint
from eshopper.products.modules import product
from eshopper.wishlist.modules import Wishlist
from eshopper import app, db, bcrypt,params
from eshopper import home
wishlist = Blueprint('wishlist', __name__)


# for individual item
@wishlist.route("/wishlist1")
def wishlist2():
    if ('user' in session):
        wishlist1 = Wishlist.query.filter_by(user=session['user']).all()
        return render_template('checkout.html', wishlist1=wishlist1)
    else:
        flash('User is not logged in, Please login before adding items to wishlist', 'danger')
        return redirect(url_for("user.login"))


@wishlist.route("/wishlist/<int:product11>")
def wishlist1(product11):
    if ('user' in session):

        wishlist1 = product.query.filter_by(productid=product11).first()
        cart1 = Wishlist(productid=wishlist1.productid, user=session['user'], productname=wishlist1.productname, productprice=wishlist1.productprice, categoryname=wishlist1.categoryname, image=wishlist1.image, brand=wishlist1.brand)
        db.session.add(cart1)
        db.session.commit()
    else:
        flash('User is not logged in, Please login before adding items to wishlist', 'danger')
        redirect(url_for("user.login"))
    return redirect(url_for("home.home1"))


@wishlist.route("/delete/<int:sno>")
def delete(sno):
    if ('user' in session):
        delete = Wishlist.query.filter_by(user=session['user'],sno=sno).first()
        db.session.delete(delete)
        db.session.commit()
    return redirect('/wishlist1')