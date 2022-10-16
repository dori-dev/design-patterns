from __future__ import annotations
from abc import ABC, abstractmethod


class Director:
    __builder: Builder = None

    def set_builder(self, builder: Builder):
        self.__builder = builder

    def get_car(self):
        car = Car()
        wheel = self.__builder.get_wheel()
        car.set_wheel(wheel)
        engine = self.__builder.get_engine()
        car.set_engine(engine)
        body = self.__builder.get_body()
        car.set_body(body)
        return car


class Car:
    def __init__(self):
        self.__wheel: Wheel = None
        self.__engine: Engine = None
        self.__body: Body = None

    def set_wheel(self, wheel):
        self.__wheel = wheel

    def set_engine(self, engine):
        self.__engine = engine

    def set_body(self, body):
        self.__body = body

    def detail(self):
        print(
            f'Wheel: {self.__wheel.size}\n'
            f'Engine: {self.__engine.hp}\n'
            f'Body: {self.__body.shape}'
        )


class Builder(ABC):
    @abstractmethod
    def get_wheel(self):
        pass

    @abstractmethod
    def get_engine(self):
        pass

    @abstractmethod
    def get_body(self):
        pass


class Benz(Builder):
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.hp = 500
        return engine

    def get_body(self):
        body = Body()
        body.shape = 'Suv'
        return body


class BMW(Builder):
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 18
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.hp = 340
        return engine

    def get_body(self):
        body = Body()
        body.shape = 'Sedan'
        return body


class Wheel:
    size = None


class Body:
    shape = None


class Engine:
    hp = None


if __name__ == '__main__':
    bmw = BMW()
    director = Director()
    director.set_builder(bmw)
    car = director.get_car()
    car.detail()
