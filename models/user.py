from peewee import Model, CharField, IntegerField, Check
from .db import db


class User(Model):
    name = CharField()
    age = IntegerField(constraints=[Check("age >= 1 AND age <= 3")])

    class Meta:
        database = db
