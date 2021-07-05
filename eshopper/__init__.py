
from flask import Flask, render_template, request, session, redirect, url_for

from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_mail import Mail
import json
from datetime import datetime
from flask_bcrypt import Bcrypt



with open('eshopper/config.json', 'r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)
app.config['SECRET_KEY'] = "super-secret-key"
app.config['UPLOAD_FOLDER'] = "C:\\Users\\Rion Alphonso\\PycharmProjects\\flask eshopper\\static\\img"
app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)





app.config.update(
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT='465',
        MAIL_USE_SSL=True,
        MAIL_USERNAME=params['gmail-user'],
        MAIL_PASSWORD=params['gmail-password']
    )
mail = Mail(app)


from eshopper import routes