"""Template pattern lives here."""

from abc import ABC, abstractclassmethod, abstractmethod


class DBRecord:
    def validate(self):
        pass

    def save(self):
        self.validate()
        print("obj stored successfully.") # db write call.


class User(DBRecord):
    def validate(self):
        print("custom validation check logic.")
        pass


user: User = User()
user.save()


class AbstractClass(ABC):
    @classmethod
    def abstract_method(cls, key: str = "key"):
        print(key)


class ConcreteClass(AbstractClass):
    __key="lol"

    def get_key(self):
        return self.__key

a = ConcreteClass()
a.abstract_method(key=a.get_key())