from copy import deepcopy


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Prototype:
    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        del self._objects[name]

    def clone(self, name, **kwargs):
        cloned_obj = deepcopy(self._objects.get(name))
        cloned_obj.__dict__.update(kwargs)
        return cloned_obj


if __name__ == '__main__':
    p1 = Person('mohammad', 17)
    prototype = Prototype()
    prototype.register('person1', p1)

    person_copy = prototype.clone('person1')
    print(person_copy.__dict__)
    print(person_copy.name is p1.name)

    person_copy = prototype.clone('person1', age=18, id=1)
    print(person_copy.__dict__)
    print(person_copy.id)
