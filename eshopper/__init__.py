
from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json
from flask_bcrypt import Bcrypt


with open('eshopper/config.json', 'r') as c:
    params = json.load(c)["params"]
app = Flask(__name__)
app.config['SECRET_KEY'] = "super-secret-key"
app.config['UPLOAD_FOLDER'] = "C:\\Users\\Rion Alphonso\\PycharmProjects\\flask eshopper\\static\\img"
app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
app.static_folder = 'static'
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


from eshopper.user.routes import user
from eshopper.home.routes import home
from eshopper.products.routes import products
from eshopper.utils.routes import utils
#from eshopper.chatbot.routes import chatbot
from eshopper.wishlist.routes import wishlist
from eshopper.cart1.routes import cart


app.register_blueprint(user)
app.register_blueprint(home)
app.register_blueprint(products)
app.register_blueprint(utils)
#app.register_blueprint(chatbot)
app.register_blueprint(wishlist)
app.register_blueprint(cart)