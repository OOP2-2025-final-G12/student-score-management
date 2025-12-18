from peewee import Model, ForeignKeyField, DateTimeField, CharField, IntegerField, Check
from .db import db
from .user import User
from .product import Product

class Order(Model):
    user = ForeignKeyField(User, backref='orders')
    product = ForeignKeyField(Product, backref='orders')
    order_date = DateTimeField()

    type = CharField(max_length=20, default='未設定')
    test_result = IntegerField(default=0, constraints=[Check("test_result >= 0 AND test_result <= 100")])

    class Meta:
        database = db
