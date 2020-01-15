from peewee import *

from models.base_model import BaseModel


class FirstName(BaseModel):
    idd = AutoField(column_name='fn_id', verbose_name='ID imienia')
    name = CharField(column_name='first_name', verbose_name='Imię', max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        table_name = 'first_name'
