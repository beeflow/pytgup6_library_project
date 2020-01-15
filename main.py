from library_options.books import Books
from library_options.users import Users
from models.book_copy import BookCopy
from models.rent_book import RentBook


def main():
    print("Wybierz opcję:")
    print("  1 - Dodaj książkę")
    print("  2 - Znajdź książkę")
    print("  3 - Dodaj użytkownika")
    print("  q - Zakończ porogram")

    option = input("> ")

    if option == 'q':
        exit()

    try:
        option = int(option)
    except ValueError:
        main()

    if option == 3:
        user_id = Users().add()
        print(f'Dodano użytkownika o ID {user_id}')

    if option == 2:
        book = Books().find()

        try:
            book_copy = BookCopy().get(book=book, is_available=True)
        except:
            print('Brak dostępnych egzemplarzy.')
            main()

        print(f'Wybrano książkę "{book}"')
        print('Dostępne opcje:')
        print('   1 - Wypożycz książkę')
        print('   * - Powrót do głównego menu')

        sub_option = input("> ")

        if sub_option == '*':
            main()

        try:
            sub_option = int(sub_option)
        except ValueError:
            main()

        if sub_option == 1:
            user = Users().find()
            if input(f'Wypożyczyć książkę "{book}" czytelnikowi {user}? [t/n]') == 't':
                RentBook(book=book_copy, reader=user).save()
                print('Książka wypożyczona :D')

    if option == 1:
        book_id = Books().add()
        print(f'Dodano książkę o ID {book_id}')

    main()

    # book = Book().get_by_id(1)
    # for i in book.authors:
    #     print(i)

    # author = Author().select().join(LastName).where(LastName.name % 'sienkiewicz')
    #
    # for book in author[0].books:
    #     print(book)
    #
    # copies = BookCopy().select().where(BookCopy.book == 1)
    # for copy in copies:
    #     print(copy)
    # #
    # rent = RentBook().select()
    # for i in rent:
    #     print(i)

    # client = LibraryClient().get_by_id(1)
    # print(client.first_name.name)


if __name__ == '__main__':
    main()
