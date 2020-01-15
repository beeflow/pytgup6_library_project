from peewee import *

from models.base_model import BaseModel
from models.first_name import FirstName
from models.last_name import LastName


class Author(BaseModel):
    id = AutoField(column_name='author_id')
    first_name = ForeignKeyField(FirstName, column_name='author_first_name_id')
    last_name = ForeignKeyField(LastName, column_name='author_last_name_id')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
