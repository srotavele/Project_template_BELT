from ..config.mysqlconnections import connectToMySQL
from flask import flash
import re
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile('\d.*[A-Z]|[A-Z].*\d')


class Recipe:
    def __init__(self,data):
        
        

    @classmethod
    def get_all(cls):
        pass

    @classmethod
    def get_one(cls, data):
        pass

    @classmethod
    def create(cls, data):
        pass
    


    @classmethod
    def update(cls, data):
        pass
    
    @classmethod
    def delete(cls, data):
        pass
