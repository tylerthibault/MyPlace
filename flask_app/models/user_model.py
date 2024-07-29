from flask_app import bcrypt
from flask_app.models import base_model
from flask import flash, session

class User(base_model.Base):
    table_name = "users"
    attributes = ['first_name', 'last_name', 'email', 'password']
    required_attributes = ['first_name', 'last_name', 'email', 'password']
    def __init__(self, data):
        super().__init__(data)

        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']

    @classmethod
    def validate_registration(cls, **data):
        # TODO validate that it is not a duplicate email
        is_valid = super().validator(**data)

        check_user_in_db = User.get(email=data['email'])

        if check_user_in_db:
            flash("User already in database", "err_users_general")
            is_valid = False

        if data['password'] != data['confirm_password']:
            flash("passwords do not match", "err_users_confirm_password")
            is_valid = False

        return is_valid
    
    @classmethod 
    def validate_login(cls, data):
        print(data)

        is_valid = True
        user_in_db = User.get(email=data['email'])
        if not user_in_db:
            flash("User/Password incorrect", "err_users_general")
        else:
            if not bcrypt.check_password_hash(user_in_db.password, data['password']):
                flash("User/Password incorrect", "err_users_general")
                is_valid = False
            else:
                session['uuid'] = user_in_db.id

        return is_valid

