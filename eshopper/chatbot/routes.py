from flask import Flask, render_template, request, session, redirect, url_for,flash,Blueprint
from eshopper import app, db, bcrypt,mail,params
from eshopper.chatbot import chatbot

chatbot = Blueprint('chatbot', __name__)

@chatbot.route("/chatbot")
def hom():
    return render_template("chatbot.html")

@chatbot.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))