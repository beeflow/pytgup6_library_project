from models.first_name import FirstName
from models.last_name import LastName
from models.library_client import LibraryClient


def main():
    try:
        first_name = FirstName(name='Zenon')
        last_name = LastName(name='Klapek')
    except:
        pass

    client = LibraryClient(first_name=first_name, last_name=last_name)
    client.save()
    print(client)

    # client = LibraryClient().get_by_id(1)
    # print(client.first_name.name)


if __name__ == '__main__':
    main()
