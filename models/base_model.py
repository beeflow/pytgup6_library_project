from peewee import *
from settings import DATABASE_CONFIG

mysql = MySQLDatabase('sda_pytgup6_test', **DATABASE_CONFIG)

class BaseModel(Model):
    class Meta:
        database = mysql