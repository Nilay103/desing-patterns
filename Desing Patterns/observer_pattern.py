### File starts here ###
#   best use case for design feed system/chat system.


# instead using interface, we can also use abstract class 
#   and define abstact methods as majority of observers 
#   will have common method logic.
from abc import abstractmethod
from random import randint


class ObserverInterface:
    observable = None
    def execute(self, msg: str):
        pass


class ObservableInterface:
    def add(self, instance):
        pass

    def remove(self, instance):
        pass

    def notify(self):
        pass


class DisplayInterface:
    def display(self):
        pass


# note we can also define Observer -> (has-a) Observable 
#   by defining observable instance for observer obj.
#   doing this, we can achieve stateless 
#   (execute doesn't required msg param, 
#   it can be fetched using self.observable.get_state())

# in current example we tried to understand push-pull model
# in push-push model, there's no need to define observable in observer
# observable can pass related data to observers in notify method directly.

class Observer:
    def __init__(self, observable) -> None:
        self.observable = observable

    @abstractmethod
    def execute(self) -> None:
        # pull
        self.display(self.observable.get_state())

    @abstractmethod
    def display(self, msg) -> str:
        print(msg)


class ObserverType1(Observer, ObserverInterface, DisplayInterface):
    pass


class ObserverType2(Observer, ObserverInterface, DisplayInterface):
    pass


class Observable(ObservableInterface):
    def __init__(self) -> None:
        self.observers = []        
        self.random_var: int = 0

    def add(self, instance: ObservableInterface) -> None:
        self.observers.append(instance)

    def remove(self, instance: ObservableInterface) -> None:
        self.observers.remove(instance)

    def notify(self) -> None:
        # push
        for observer in self.observers:
            observer.execute()

    def get_state(self) -> int:
        return self.random_var

    def set_state(self, value) -> None:
        self.random_var = value
        self.notify()


observable: Observable = Observable()
observer_a: ObserverType1 = ObserverType1(observable=observable)
observer_b: ObserverType2 = ObserverType2(observable=observable)
observable.add(observer_a)
observable.add(observer_b)
observable.set_state(randint(1, 100))
observable.set_state(randint(1, 100))
