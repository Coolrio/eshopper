
from flask import Flask, render_template, request, session, redirect, url_for

from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_mail import Mail
import json
import os
import math
from datetime import datetime

with open('config.json', 'r') as c:
    params = json.load(c)["params"]
local_server = True
app = Flask(__name__)
app.config['SECRET_KEY'] = "super-secret-key"
app.config['UPLOAD_FOLDER'] = "C:\\Users\\Rion Alphonso\\PycharmProjects\\flask eshopper\\static\\img"
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password']
)
mail = Mail(app)
if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)


class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    subject = db.Column(db.String(50), nullable=True)
    msg = db.Column(db.String(500), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(50), nullable=False)


class login_user(db.Model):
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

@app.route("/")
def home():

    product_pro = product.query.filter_by().all()[0:params['no_of_posts']]
    brand=product.query.filter_by(brand="samsung").all()[0:params['no_of_posts']]
    wired_earphone = product.query.filter_by(categoryname="wired_earphone").all()[0:params['no_of_posts']]
    laptop=product.query.filter_by(categoryname="laptop").all()[0:params['no_of_posts']]
    mobile = product.query.filter_by(categoryname="mobilephones").all()[0:params['no_of_posts']]
    tv = product.query.filter_by(categoryname="tv").all()[0:3]
    washing = product.query.filter_by(categoryname="washingmachine").all()[0:params['no_of_posts']]

    return render_template('index.html', product=product_pro, brand=brand, mobile=mobile, wired_earphone=wired_earphone
                           ,laptop=laptop,washing=washing,tv=tv)


@app.route("/login", methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            username = request.form.get("name")
            userpass = request.form.get("password")

            login = login_user.query.filter_by(email=username).first()

            if username == login.email and userpass == login.password:
                session['name'] = username
                return render_template('index.html')
    except:
            return render_template('404.html')
    return render_template('login.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if (request.method == 'POST'):
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        dob = request.form.get('dob')
        address = request.form.get('address')
        pincode = request.form.get('pincode')
        city = request.form.get('city')
        landmark = request.form.get('landmark')
        state = request.form.get('state')
        country = request.form.get('country')
        houseno = request.form.get('housenumber')
        password = request.form.get('password')
        gender = request.form.getlist('gender')
        confirmpassword = request.form.get('currentpassword')

        entry = login_user(firstname=firstname, lastname=lastname, email=email, phone=phone, dob=dob,
                               address=address,
                               pincode=pincode, city=city, landmark=landmark, houseno=houseno, state=state,
                               country=country,
                               password=password, gender=gender)
        db.session.add(entry)
        db.session.commit()
        return redirect ("/login")
    return render_template('register.html')


@app.route("/logout")
def logout():
    session.pop('user')
    return redirect("/index.html")






@app.route("/checkout", methods=['GET', 'POST'])
def checkout():
    if ('user' in session and session['user'] == params['admin_user']):
        return render_template('checkout.html', params=params)
    if request.method == 'POST':
        username = request.form.get("name")
        userpass = request.form.get("password")
        if (username == params['admin_user'] and userpass == params['admin_password']):
            session['name'] = username

            return render_template('checkout.html')
    return render_template('login.html', params=params)


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
    return render_template('contact.html', params=params)


app.run(debug=True)
