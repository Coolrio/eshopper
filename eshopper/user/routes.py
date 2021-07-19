from flask import Flask, render_template, request, session, redirect, url_for,flash,Blueprint
from eshopper import app, db, bcrypt
from eshopper.user.modules import user_login
from eshopper.user.forms import RegistrationForm


user = Blueprint('user', __name__)

@user.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if (request.method == 'POST'):
        firstname = form.firstname.data
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
        return redirect(url_for('user.login'))
    return render_template('register1.html', title='Register', form=form)


@user.route("/login", methods=['GET', 'POST'])
def login():

        if request.method == 'POST':
            username = request.form.get("name")
            userpass = request.form.get("password")
            login = user_login.query.filter_by(email=username).first()

            if login and bcrypt.check_password_hash(login.password, userpass):
                session['user'] = username

                return redirect(url_for('home.home1'))

            else:
                flash('email id or password does not exists','danger')

        return render_template('login (1).html', title='Login')




@user.route("/account", methods=['GET', 'POST'])
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
            if request.method == 'POST':
                loginn1 = user_login.query.filter_by(email=session['user']).first()
                loginn1.firstname=firstname
                loginn1.lastname=lastname
                loginn1.email=email
                loginn1.phone=mobile
                loginn1.pincode=pincode
                loginn1.city=city
                loginn1.landmark=landmark
                loginn1.state=state
                loginn1.country=country
                loginn1.houseno=houseno
                loginn1.address=address
                db.session.commit()
                return redirect('/account')
            return render_template('userprofile.html', loginn=loginn)
        else:
            return redirect(url_for('user,login'))
    except:
        flash('User is not logged in', 'danger')
        return redirect(url_for('user.login'))

@user.route("/logout")
def logout():
    session.pop('user')
    return redirect("/home")
