import datetime

from peewee import *

from models.base_model import BaseModel
from models.book_copy import BookCopy
from models.library_client import LibraryClient


class RentBook(BaseModel):
    id = AutoField(column_name='rb_id')
    rent_date = DateTimeField(column_name='rb_rent_date', default=datetime.datetime.now, null=False)
    return_date = DateTimeField(column_name='rb_return_date', null=True)
    book = ForeignKeyField(BookCopy, column_name='rb_bc_id', null=False)
    reader = ForeignKeyField(LibraryClient, column_name='rb_lc_id')
