from peewee import *

from models.base_model import BaseModel


class LastName(BaseModel):
    id = AutoField(column_name='ln_id')
    name = CharField(column_name='last_name', max_length=50, unique=True)

    class Meta:
        table_name = 'last_name'
