from peewee import Model, CharField, DecimalField, Check
from .db import db

class Product(Model):
    name = CharField()
    price = DecimalField(constraints=[
        Check('rating >= 1 AND rating <= 3')
    ])

    class Meta:
        database = db