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
    if not User.validate_signup(request.form):
        return redirect('/')
    
    hash_me = bcrypt.generate_password_hash(request.form['password'])
    
    data ={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': hash_me
        }
    user_id = User.create(data)
    session['client'] = user_id
    
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')