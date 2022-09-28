from typing import List


class Observer:
    def __init__(self):
        self._observers: List[Signal] = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)


class Data(Observer):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


class Signal:
    def update(self, subject: Observer):
        pass


class One(Signal):
    def update(self, subject: Data):
        print(f'new "{subject.name}" data: {subject.data}')


class Two(Signal):
    def update(self, subject: Data):
        print(f'new "{subject.name}" data: {subject.data}')


if __name__ == '__main__':
    d1 = Data('first')
    d1.attach(One())
    d2 = Data('second')
    d2.attach(Two())
    d1.data = 5
    d2.data = 3
