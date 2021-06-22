from flask_app.config.mysqlconnections import connectToMySQL
from flask import flash
import re
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile('\d.*[A-Z]|[A-Z].*\d')

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        pass

    @classmethod
    def create(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());'
        
        results = connectToMySQL('recipes_schema').query_db(query, data)
        return results
    
    @classmethod
    def get_one(cls, data):
        pass

    @classmethod
    def update(cls, data):
        pass
    
    @classmethod
    def delete(cls, data):
        pass
    
    @staticmethod
    def validate_signup(post_data):
        is_valid = True
        if len(post_data['first_name']) < 2:
            flash('First Name must be at least two characters.')
            is_valid = False
        if len(post_data['last_name']) < 2:
            flash('Last Name must be at least two characters.')
            is_valid = False
        if not EMAIL_REGEX.match(post_data['email']):
            flash('Email Address is not valid')
            is_valid = False
        if len(post_data['password']) < 8
            flash('Password must be at least 8 characters')
        if not PASSWORD_REGEX.match(post_data['password']):
            flash('Password must contain ONE capital letter and ONE number.')
        else:
            if post_data['password'] != post_data['confirm_password']:
                flash('Passwords do not match.')
                is_valid = False
        return 
    
    @staticmethod 
    def validate_login(post_data):
        db_user = User.get_by_email({'email: post_data['email']})
        if not db_user;
            flash('Invalid credentials.')
            return False
        if not bcrypt.check_password_hash(db_user.password.post_data['password']):
            flash('Invalid credentials')
                return False
                
        return True
        