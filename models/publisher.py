from peewee import *

from models.base_model import BaseModel


class Publisher(BaseModel):
    id = AutoField(column_name='publisher_id')
    name = CharField(column_name='publisher_name', max_length=100, null=False)

    def __str__(self):
        return self.name