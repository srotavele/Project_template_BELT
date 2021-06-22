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
        self.id =  data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.descriptiom = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.time = data['time']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM recipes;'
        results = connectToMySQL('recipes_schema').query_db(query)
        
        recipes = []
        for row in results:
            recipes.append(Recipes(row))
        return recipes
    

    @classmethod
    def create_recipe(cls, data):
        query = 'INSERT INTO recipes (user_id, name, description, instructions, date_made, time, created_at, updated_at) VALUES (%(user_id)s, %(name)s, %(description)s, %(instructions)s, %(date_made)s, %(time)s, NOW(), NOW());'
        
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
