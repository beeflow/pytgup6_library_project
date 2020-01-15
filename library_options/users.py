from peewee import JOIN

from models.first_name import FirstName
from models.last_name import LastName
from models.library_client import LibraryClient


class Users:
    """ Zarządzanie użytkownikami biblioteki. """

    def add(self) -> int:
        """ Dodawanie nowych użytkowników do bazy. """
        print('Dodawanie nowego użytkownika')

        first_name = FirstName().get_or_create(name=input('Podaj imię: '))[0]
        last_name = LastName().get_or_create(name=input('Podaj nazwisko: '))[0]

        first_name.save()
        last_name.save()

        client = LibraryClient(first_name=first_name, last_name=last_name)
        client.save()

        return client.id

    def find(self) -> LibraryClient:
        print('Znajdź użytkownika')
        username = input('  imię i nazwisko: ')

        first_name, last_name = username.split(' ')

        user = LibraryClient().get_or_create(
            first_name=FirstName().get_or_create(name=first_name)[0],
            last_name=LastName().get_or_create(name=last_name)[0]
        )[0]

        return user

    def find_by_last_name(self):
        ln = input('Podaj nazwisko: ')

        users = LibraryClient().select().\
            join(LastName, JOIN.LEFT_OUTER).\
            switch(LibraryClient).\
            join(FirstName, JOIN.LEFT_OUTER).\
            where(LastName.name.contains(ln)).\
            order_by(FirstName.name.desc())

        for user in users:
            print(user)
