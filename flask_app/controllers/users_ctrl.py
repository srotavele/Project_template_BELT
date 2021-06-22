from flask import render_template, request, session, redirect, flash
from flask_app.config.mysqlconnections import connectToMySQL
from flask_app.models.users_mdl import User
from flask_bcrypt import Bcrypt
from flask_app import app
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign_up', methods = ['POST'])
def sign_up():
    