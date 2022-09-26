from abc import ABC, abstractmethod


class Context:
    def __init__(self, direction, sentence):
        self._direction: Direction = direction()
        self.sentence = sentence

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        self._direction = direction

    def sorting(self):
        return self._direction.direct(self.sentence)


class Direction(ABC):
    @abstractmethod
    def direct(self, data):
        pass


class Right(Direction):
    def direct(self, data):
        print(data[::-1])


class Left(Direction):
    def direct(self, data):
        print(data)


if __name__ == '__main__':
    text = Context(Right, 'Hello World...')
    text.sorting()
    text = Context(Left, 'Hello World...')
    text.sorting()
