from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app import app

bcrypt = Bcrypt(app)

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

@classmethod
def save(cls, data):
    query = "INSERT INTO usuarios (nombre, apellido, email, password) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s);"
    result = connectToMySQL('usuarios').query_db(query, data)
    return result

@classmethod
def get_by_email(cls, data):
    query = "SELECT * FROM usuarios WHERE email = %(email)s;"
    result = connectToMySQL('usuarios').query_db(query, data)
    if len(result) < 1:
        return False
    return cls(result[0])
@classmethod
def get_by_id(cls, data):
    query = "SELECT * FROM usuarios WHERE id = %(id)s;"
    result = connectToMySQL('usuarios').query_db(query, data)
    if len(result) < 1:
        return False
    return cls(result[0])