from flask import Flask, render_template, request, session, redirect, url_for, flash, Blueprint
from eshopper import app, db, bcrypt, mail
import random
from eshopper.user.modules import user_login
from eshopper.utils.modules import Contact
from flask_mail import Message
from eshopper.user.forms import RegistrationForm, RequestResetForm, ResetPasswordForm

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
            flash('email id or password does not exists', 'danger')

    return render_template('login (1).html', title='Login')


@user.route("/account", methods=['GET', 'POST'])
def account():
    try:
        loginn = user_login.query.filter_by(email=session['user']).first()
        if ('user' in session):
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
                loginn1.firstname = firstname
                loginn1.lastname = lastname
                loginn1.email = email
                loginn1.phone = mobile
                loginn1.pincode = pincode
                loginn1.city = city
                loginn1.landmark = landmark
                loginn1.state = state
                loginn1.country = country
                loginn1.houseno = houseno
                loginn1.address = address
                db.session.commit()
                return redirect('/account')
            return render_template('userprofile.html', loginn=loginn)
        else:
            return redirect(url_for('user,login'))
    except:
        flash('User is not logged in', 'danger')
        return redirect(url_for('user.login'))


@user.route("/forgotpasswod", methods=['GET', 'POST'])
def forgot_password():

    if request.method=='post':
        email = request.form.get('email')
        otp = random.randint(1111, 9999)
        mail.send_message('New message from admin',
                      sender='admin',
                      recipients=[email],
                      body="do not share this otp with other" + "\n" + str(otp)
                      )
        otp_field = request.form.get('otp')
        loginn1 = user_login.query.filter_by(email=email).first()
        if otp_field == otp:
            redirect('/newpassword')
        else:
            flash('entered wrong otp')
    return render_template('forgotpassword.html')


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)


@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if ('user' in session):
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = user_login.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('user.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if ('user' in session):
        return redirect(url_for('home.home1'))
    user = user_login.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('user.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)

@user.route("/logout")
def logout():
    session.pop('user')
    return redirect("/home")
