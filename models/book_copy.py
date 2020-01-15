from peewee import *

from models.base_model import BaseModel
from models.book import Book


class BookCopy(BaseModel):
    BOOK_CONDITIONS = ('good', 'bad', 'terrible')

    id = AutoField(column_name='bc_id')
    condition = CharField(column_name='bc_condition', choices=BOOK_CONDITIONS, default='good')
    is_available = BooleanField(default=True)
    book = ForeignKeyField(Book, column_name='bc_book_id', null=False)

    def __str__(self):
        return f'{self.book} [{self.id}]'
