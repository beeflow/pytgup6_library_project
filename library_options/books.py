from typing import List

from models.author import Author
from models.book import Book
from models.first_name import FirstName
from models.last_name import LastName
from models.publisher import Publisher


class Books:
    def add(self) -> int:
        print('Dodawanie książki')
        print('-----------------')

        title = input('Tytuł: ')
        isbn = input('ISBN: ')
        description = input('Opis (opcjonalnie): ')
        publisher = Publisher().get_or_create(name=input('Nazwa wydawnictwa: '))[0]

        next_author = 't'
        authors = []

        while next_author == 't':
            authors.append(input('Imię i nazwisko autora: '))
            next_author = input('Następny autor? [t/n]')

        authors = self.add_authors(authors)
        book = Book(title=title, isbn=isbn, description=description, publisher=publisher)
        book.save()

        book.authors = authors
        book.update()

        return book.id

    def find(self) -> Book:
        print('Wyszukiwanie książek')
        books = Book().select().where(Book.title.contains(input('Podaj tytuł: ')))

        for book in books:
            print(f'{book.id} | {book.title}')

        if not books:
            self.find()

        while True:
            try:
                return Book().get_by_id(int(input('Wybierz książkę: ')))
            except:
                print('Nie wybrano książki...')

    def add_authors(self, authors: List[str]) -> List[Author]:
        """Dodawanie nowych autorów."""
        result = []

        for author_name in authors:
            try:
                first_name, last_name = author_name.split(' ')
            except ValueError:
                first_name, last_name = author_name, None

            author = Author().get_or_create(
                first_name=FirstName().get_or_create(name=first_name)[0],
                last_name=LastName().get_or_create(name=last_name)[0] if last_name else None
            )[0]

            result.append(author)

        return result
