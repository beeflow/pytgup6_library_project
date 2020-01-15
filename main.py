from library_options.users import Users


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

    main()

    # book = Book().get_by_id(1)
    # for i in book.authors:
    #     print(i)

    # author = Author().select().join(LastName).where(LastName.name == 'sienkiewicz')
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
