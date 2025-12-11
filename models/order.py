from peewee import Model, ForeignKeyField, DateTimeField, CharField, IntegerField
from .db import db
from .user import User
from .product import Product

class Order(Model):
    user = ForeignKeyField(User, backref='orders')
    product = ForeignKeyField(Product, backref='orders')
    order_date = DateTimeField()

    type = CharField(max_length=20, default='未設定')
    test_result = IntegerField(default=0)

    class Meta:
        database = db
