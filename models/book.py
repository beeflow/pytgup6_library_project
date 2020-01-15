from peewee import *

from models.author import Author
from models.base_model import BaseModel
from models.publisher import Publisher


class Book(BaseModel):
    id = AutoField(column_name='book_id')
    title = CharField(max_length=100, column_name='book_title', null=False)
    isbn = CharField(max_length=13, column_name='book_isbn', null=False)
    description = CharField(max_length=4000, column_name='book_description', null=True)
    publisher = ForeignKeyField(Publisher, column_name='book_publisher_id', null=False)
    authors = ManyToManyField(Author, backref='books')

    def __str__(self):
        return self.title
