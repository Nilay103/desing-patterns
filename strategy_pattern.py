### Understand strategy patterns using sample examples ###


class Duck:
    """parent class, contains multiple common methods
    """    
    def display(self):
        print("logic common")

    def fly(self):
        print("logic common")

    def temp(self):
        print("Some temp logic")


class CityDuck(Duck):
    """Child class type 1

    Args:
        Duck (_type_): _description_
    """
    def display(self):
        print("logic 1")

    def fly(self):
        return super().fly()

    def temp(self):
        print("Some temp logic")

class VillageDuck(Duck):
    """Child class type 2

    Args:
        Duck (_type_): _description_
    """
    def display(self):
        print("logic 2")

    def fly(self):
        return super().fly()


class PlasticDuck(Duck):
    """Child class Type 3

    Args:
        Duck (_type_): _description_
    """
    def display(self):
        print("logic 3")

    def fly(self):
        print("logic A")

    def temp(self):
        print("Some temp logic")


class WoodDuck(Duck):
    """Child class Type 4

    Args:
        Duck (_type_): _description_
    """
    def display(self):
        print("logic 4")

    def fly(self):
        print("logic A")


class RubberDuck(Duck):
    """Child class Type 5

    Args:
        Duck (_type_): _description_
    """
    def display(self):
        print("logic 5")

    def fly(self):
        print("logic A")

# As you see, fly method can be utilised. To do that, 
#   do I really need to make another parent class ShowPieceDuck?
#   what will happen when Duck has some temp method and some ShowPieceDuck and some LiveDuck inherits the logic

# Solution:
#   darek method na parent class banai devana. So suppose fly method na 2 logics che toh
#   Class Fly, Class WingFlying, Class NoFlying define kari devanu and
#   Duck class nu Fly class jode composite relation (has-a) define kari levanu

# Conclusion: 
#   Yes, Inheritance is useful, but can raise complications to your complex systems.
#   Define (has-a) behavior for parent class methods and for each has-a behavior class (as a parent), 
#   define diffrent sub class for each type of method algo.

#                       Parent
#                      /      \
#           ClassMethod1     ClassMethod2
#           /    \                     /     \
#    ClsStrategy1  ClsStrategy2   ClsStrategy1  ClsStrategy2
#


class StrategyDisplay:
    def __init__(self) -> None:
        print("StrategyDisplay Constructor Called")

    def display_type_A(self) -> None:
        print("display type A")

    def display_type_B(self) -> None:
        print("display type B")


class StrategyFly:
    def __init__(self) -> None:
        print("StrategyFly Constructor Called")

    def fly_type_A(self) -> None:
        print("fly type A")
    
    def fly_type_B(self) -> None:
        print("fly type B")


class Duck:
    def __init__(self) -> None:
        print("Duck Constructor Called")
        self.display_strategy = StrategyDisplay()
        self.fly_strategy = StrategyFly()


class CityDuck(Duck):
    def display(self) -> None:
        self.display_strategy.display_type_A()

    def fly(self) -> None:
        self.fly_strategy.fly_type_A()


class VillageDuck(Duck):
    def display(self) -> None:
        self.display_strategy.display_type_B()

    def fly(self) -> None:
        self.fly_strategy.fly_type_A()


class WoodDuck(Duck):
    def display(self) -> None:
        self.display_strategy.display_type_A()

    def fly(self) -> None:
        self.fly_strategy.fly_type_B()


class PlasticDuck(Duck):
    def display(self) -> None:
        self.display_strategy.display_type_B()

    def fly(self) -> None:
        self.fly_strategy.fly_type_B()
