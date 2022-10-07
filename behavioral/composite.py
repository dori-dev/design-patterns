from abc import ABC, abstractmethod
from typing import List

TAB = '  '

class World(ABC):
    def __init__(self, name):
        self.name = name
        self.children: List[World] = []

    def add(self, object):
        self.children.append(object)

    def remove(self, object):
        self.children.remove(object)

    @abstractmethod
    def show(self):
        pass


class Being(World):
    def __init__(self, name):
        super().__init__(name)

    def show(self):
        print(f'Being Composite {self.name}')
        for child in self.children:
            child.show()


class Animal(World):
    def __init__(self, name):
        super().__init__(name)

    def show(self):
        print(f'{TAB}Animal Composite {self.name}')
        for child in self.children:
            child.show()


class Human(World):
    def __init__(self, name):
        super().__init__(name)

    def show(self):
        print(f'{TAB}Human Composite {self.name}')
        for child in self.children:
            child.show()


class Cat(World):
    def __init__(self, name):
        super().__init__(name)

    def show(self):
        print(f'{TAB*2}Cat Leaf {self.name}')


class Dog(World):
    def __init__(self, name):
        super().__init__(name)

    def show(self):
        print(f'{TAB*2}Dog Leaf {self.name}')


class Male(World):
    def __init__(self, name):
        super().__init__(name)

    def show(self):
        print(f'{TAB*2}Male Leaf {self.name}')


class Female(World):
    def __init__(self, name):
        super().__init__(name)

    def show(self):
        print(f'{TAB*2}Female Leaf {self.name}')


if __name__ == '__main__':
    cat = Cat('Missy')
    dog = Dog('Jerry')
    animals = Animal('animals')
    animals.add(cat)
    animals.add(dog)

    male = Male('Mohammad')
    female = Female('Sara')
    humans = Human('humans')
    humans.add(male)
    humans.add(female)

    being = Being('all')
    being.add(animals)
    being.add(humans)

    being.show()
