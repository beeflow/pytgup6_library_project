from peewee import *

from settings import DATABASE_CONFIG, DATABASE_NAME

mysql = MySQLDatabase(DATABASE_NAME, **DATABASE_CONFIG)


class BaseModel(Model):
    class Meta:
        database = mysql
        legacy_table_names = False
