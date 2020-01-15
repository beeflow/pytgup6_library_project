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
        book = Book(title=title, isbn=isbn, description=description, publisher=publisher, authors=authors)

        book.save()

        return book.id

    def add_authors(self, authors: List[str]) -> List[Author]:
        """Dodawanie nowych autorów."""
        result = []

        for author_name in authors:
            first_name, last_name = author_name.split(' ')
            author = Author(
                first_name=FirstName().get_or_create(name=first_name)[0],
                last_name=LastName().get_or_create(name=last_name)[0] if last_name else None
            )
            author.save()
            result.append(author)

        return result
