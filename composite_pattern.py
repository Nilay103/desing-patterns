"""Composite Pattern lives here."""

from abc import ABC


class EmployeeHierarchy(ABC):
    def show_details(self):
        pass


class Leaf(EmployeeHierarchy):
    _position = None

    def __set_position(self, position):
        self._position = position

    def get_position(self):
        return self._position

    def show_details(self):
        print(self.get_position())


class Composite(EmployeeHierarchy):
    def __init__(self) -> None:
        self._children = []
        self._position = None

    def __set_position(self, position):
        self._position = position

    def add_reporter(self, node: EmployeeHierarchy):
        self._children.append(node)

    def remove_reporter(self, node: EmployeeHierarchy):
        self._children.remove(node)

    def show_details(self):
        print(self._position)
        for child in self._children:
            child.show_details()


if __name__ == "__main__":
    leaf_a: Leaf = Leaf()
    leaf_a._Leaf__set_position("BE Developer: Nilay")

    leaf_b: Leaf = Leaf()
    leaf_b._Leaf__set_position("BE Developer: Prashant")

    leaf_c: Leaf = Leaf()
    leaf_c._Leaf__set_position("FE Developer: Atif")

    leaf_d: Leaf = Leaf()
    leaf_d._Leaf__set_position("FE Developer: Aman")

    manager_a: Composite = Composite()
    manager_a.add_reporter(leaf_a)
    manager_a.add_reporter(leaf_b)
    manager_a._Composite__set_position("BE Manager")

    manager_b: Composite = Composite()
    manager_b.add_reporter(leaf_c)
    manager_b.add_reporter(leaf_d)
    manager_b._Composite__set_position("FE Manager")

    director: Composite = Composite()
    director.add_reporter(manager_a)
    director.add_reporter(manager_b)
    director._Composite__set_position("Director")

    director.show_details()
