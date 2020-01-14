from peewee import *

from models.base_model import BaseModel
from models.first_name import FirstName
from models.last_name import LastName


class LibraryClient(BaseModel):
    id = AutoField(column_name='lc_id')

    first_name = ForeignKeyField(
        FirstName,
        verbose_name='First name',
        column_name='lc_first_name_id'
    )

    last_name = ForeignKeyField(
        LastName,
        verbose_name='Last name',
        column_name='lc_last_name_id'
    )

    class Meta:
        table_name = 'library_client'