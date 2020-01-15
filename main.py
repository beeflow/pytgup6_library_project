from models.author import Author
from models.book_copy import BookCopy
from models.last_name import LastName
from models.rent_book import RentBook


def main():
    # book = Book().get_by_id(1)
    # print(book.authors[0])

    author = Author().select().join(LastName).where(LastName.name == 'sienkiewicz')

    for book in author[0].books:
        print(book)

    copies = BookCopy().select().where(BookCopy.book == 1)
    for copy in copies:
        print(copy)

    rent = RentBook().select()
    for i in rent:
        print(i)

    # client = LibraryClient().get_by_id(1)
    # print(client.first_name.name)


if __name__ == '__main__':
    main()
