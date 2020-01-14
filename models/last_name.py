from peewee import *

from models.base_model import BaseModel


class LastName(BaseModel):
    id = AutoField(column_name='ln_id')
    name = CharField(column_name='last_name', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        table_name = 'last_name'
