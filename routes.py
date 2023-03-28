from flask import flask
from app import app
from modules import User

@app.route('signup',methods=['GET'])
def signup():
    return User().signup()
    