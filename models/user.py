from peewee import Model, CharField, IntegerField, Check
from .db import db

class User(Model):
    name = CharField()
    age = IntegerField(constraints=[
        Check('rating >= 1 AND rating <= 3')
    ])

    class Meta:
        database = db