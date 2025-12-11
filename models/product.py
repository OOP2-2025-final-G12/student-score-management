from peewee import Model, CharField, DecimalField
from .db import db
from peewee import Check

class Product(Model):
    name = CharField()
    price = DecimalField(constraints=[
        Check('rating >= 1 AND rating <= 3')
    ])

    class Meta:
        database = db