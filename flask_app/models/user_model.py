from flask_app.models import base_model
from flask import flash, session

class User(base_model.Base):
    table_name = "users"
    attributes = ['first_name', 'last_name', 'email', 'password']
    required_attributes = ['first_name', 'last_name', 'email', 'password']
    def __init__(self, data):
        super().__init__(data)

        # TODO: create attributes
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']