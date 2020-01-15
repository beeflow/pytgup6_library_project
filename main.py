from library_options.books import Books
from library_options.users import Users
from models.book_copy import BookCopy
from models.rent_book import RentBook


def main():
    print("Wybierz opcję:")
    print("  1 - Dodaj książkę")
    print("  2 - Znajdź książkę")
    print("  3 - Dodaj użytkownika")
    print("  4 - Znajdź użytkownika")
    print("  q - Zakończ porogram")

    option = input("> ")

    if option == 'q':
        exit()

    try:
        option = int(option)
    except ValueError:
        main()

    if option == 4:
        Users().find_by_last_name()

    if option == 3:
        user_id = Users().add()
        print(f'Dodano użytkownika o ID {user_id}')

    if option == 2:
        book = Books().find()
        book_copy = None

        print(f'Wybrano książkę "{book}"')
        print('Dostępne opcje:')
        try:
            book_copy = BookCopy().get(book=book, is_available=True)
            print('   1 - Wypożycz książkę')
        except:
            print('   - - Brak dostępnych egzemplarzy.')
        print('   2 - Dodaj egzemplarz')
        print('   * - Powrót do głównego menu')

        sub_option = input("> ")

        if sub_option == '*':
            main()

        try:
            sub_option = int(sub_option)
        except ValueError:
            main()

        if sub_option == 2:
            bc = Books().add_copy(book)
            print(f'Kopia dodana pod ID {bc.id}')
            main()

        if sub_option == 1 and book_copy:
            user = Users().find()
            if input(f'Wypożyczyć książkę "{book}" czytelnikowi {user}? [t/n]') == 't':
                RentBook(book=book_copy, reader=user).save()
                print('Książka wypożyczona :D')

    if option == 1:
        book_id = Books().add()
        print(f'Dodano książkę o ID {book_id}')

    main()


if __name__ == '__main__':
    main()
