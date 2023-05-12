from abc import abstractmethod
from random import choice


class Animal:
    @abstractmethod
    def talk(self):
        print("Talk")

    @abstractmethod
    def description(self):
        print("Abstract Description")


class Dog(Animal):
    def talk(self):
        print("Bark")

    def description(self):
        print("Dog description")


class Cat(Animal):
    def talk(self):
        print("Meaw")

    def description(self):
        print("Cat Description")


class Lion(Animal):
    def talk(self):
        print("Roar")

    def description(self):
        print("Lion Description")


class AnimalFactory:
    def __init__(self) -> None:
        self.animals_set = [Dog.__name__, Cat.__name__, Lion.__name__]

    def pick_animal(self):
        globals()[choice(self.animals_set)]().talk()

AnimalFactory().pick_animal()
