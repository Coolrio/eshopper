from flask import Flask, render_template, request, session, redirect, url_for,flash,Blueprint
from datetime import datetime
from eshopper import app, db,mail,params
from eshopper.utils.modules import Contact


utils = Blueprint('utils', __name__)



@utils.route("/contact", methods=['GET', 'POST'])
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

