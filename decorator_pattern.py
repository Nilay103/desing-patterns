"""Decorator pattern lives here. Example of calculating starbucks coffee price
    Better example can be, string operations on input streams (bold, italic, underline etc)
"""

class Bevarage:
    """ Abstract class to manage all kind of bevarages"""
    def show_description(self) -> None:
        print("General Description")

    def cost(self) -> int:
        return 0


class AddOns(Bevarage):
    """ Abstract class to manage all types of add ons for a bevarage.
        Uses Inheritance (calls bevarage abstract class)
        &
        Uses Compositions (has-a) relation with bevarage class
    """
    def __init__(self, bevarage) -> None:
        self.bevarage = bevarage

    
class WhippedMilk(AddOns):
    def cost(self) -> int:
        return self.bevarage.cost() + 5


class Caramel(AddOns):
    def cost(self) -> int:
        return self.bevarage.cost() + 7


class Decaf(Bevarage):
    def cost(self) -> int:
        return 20


class Expresso(Bevarage):
    def cost(self) -> int:
        return 25


class Tea(Bevarage):
    def cost(self) -> int:
        return 15

decaf_coffee = Decaf()
expresso_coffee = Expresso()
decaf_coffee_with_caremal = Caramel(decaf_coffee)
print(decaf_coffee_with_caremal.cost())
decaf_coffee_with_caremal_and_milk = WhippedMilk(Caramel(decaf_coffee))
print(decaf_coffee_with_caremal_and_milk.cost())

# TODO apply init method and check number of method calls.
