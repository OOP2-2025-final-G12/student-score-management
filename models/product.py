from peewee import Model, CharField, DecimalField, Check
from .db import db

class Product(Model):
    name = CharField()
    price = CharField()

    class Meta:
        database = db