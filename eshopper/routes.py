from flask import Flask, render_template, request, session, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json
import os
import math
from datetime import datetime
from eshopper import app, db, bcrypt,mail,c,params
from eshopper.modules import Contact, user_login, product
from eshopper.forms import RegistrationForm, LoginForm




@app.route("/")
@app.route("/home")
def home():

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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if (request.method == 'POST'):



        firstname =form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        phone = form.phonenumber.data
        dob = request.form.get('dob')
        address = form.address.data
        pincode = form.pincode.data
        city = form.city.data
        landmark = form.landmark.data
        state = form.state.data
        country = form.country.data
        houseno = form.houseno.data
        gender = request.form.getlist('gender')
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        user = user_login(firstname=firstname, lastname=lastname, email=email, phone=phone, dob=dob,
                               address=address,
                               pincode=pincode, city=city, landmark=landmark, houseno=houseno, state=state,
                               country=country,
                               password=hashed_password, gender=gender)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register1.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():

        if request.method == 'POST':
            username = request.form.get("name")
            userpass = request.form.get("password")
            login = user_login.query.filter_by(email=username).first()

            if login and bcrypt.check_password_hash(login.password, userpass):
                session['user'] = username
                return redirect(url_for('home'))

            else:
                flash('email id or password does not exists','danger')

        return render_template('login (1).html', title='Login')




@app.route("/account")
def account():
    try:
        loginn=user_login.query.filter_by(email=session['user']).first()
        if ('user' in session ):
            firstname = request.form.get('name')
            lastname = request.form.get('lastname')
            email = request.form.get('email')
            mobile = request.form.get('mobilenumber')
            address = request.form.get('address')
            city = request.form.get('city')
            pincode = request.form.get('pincode')
            landmark = request.form.get('landmark')
            state = request.form.get('state')
            country = request.form.get('country')
            houseno = request.form.get('houseno')
            if request.method == 'post':
                loginn.firstname=firstname
                loginn.lastname=lastname
                loginn.email=email
                loginn.phone=mobile
                loginn.pincode=pincode
                loginn.city=city
                loginn.landmark=landmark
                loginn.state=state
                loginn.country=country
                loginn.houseno=houseno
                loginn.address=address
                db.session.commit()
                return redirect('account')
            return render_template('userprofile.html', loginn=loginn)
        else:
            return redirect(url_for('login'))
    except:
        flash('User is not logged in', 'danger')
        return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect("/home")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if (request.method == 'POST'):
        name = request.form.get('username')
        email = request.form.get('email')
        phone = request.form.get('phone')
        subject = request.form.get('sub')
        message = request.form.get('message')
        entry = Contact(name=name, phone=phone, subject=subject, msg=message, date=datetime.now(), email=email)
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients=[params['gmail-user']],
                          body=message + "\n" + phone
                          )
       
    return render_template('contact.html')

# for individual item

@app.route("/productname/<string:product11>", methods=['GET'])
def post_route(product11):
    int (product11)
    product1 = product.query.filter_by(productid=product11).first()
    return render_template('product-details.html', product1=product1)

# for sub brand item like samsung/mobilephones

@app.route("/productbrand/<string:brands>/<string:item>", methods=['GET'])
def post_route1(brands,item):
    brandname = product.query.filter_by(brand=brands,categoryname=item).all()

    return render_template('productpage.html', brandname=brandname)



@app.route("/productbrand/<string:brand1>", methods=['GET'])
def post_route2(brand1):

    brandname1 = product.query.filter_by(brand=brand1).all()
    return render_template('productpage.html', brandname1=brandname1)



@app.route("/productcategory/<string:item>", methods=['GET'])
def post_route3(item):

    brandcategory = product.query.filter_by(categoryname=item).all()
    return render_template('productpage.html', brandcategory=brandcategory)

@app.route("/productpage")
def productpage():

    product_pro = product.query.filter_by().all()
    try:
        loginn = user_login.query.filter_by(email=session['user']).first()
        if 'user' in session:
            name=loginn.firstname
    except:
        name=""
    return render_template('productpage.html', product=product_pro)