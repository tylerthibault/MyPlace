from flask_app.models import base_model
from flask import flash, session

class Budget(base_model.Base):
    table_name = "budgets"
    attributes = ['name', 'is_active']
    required_attributes = ['name', 'is_active']


    def __init__(self, data):
        super().__init__(data)

        self.name = data['name']
        self.is_active = data['is_active']

    @classmethod
    def get_all(cls, data):
        # query = "SELECT * FROM budgets WHERE "
        pass