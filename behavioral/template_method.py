from abc import ABC, abstractmethod


class Top(ABC):
    def template_method(self):
        self.first_common()
        self.second_common()
        self.third_require()
        self.fourth_require()
        self.hook()

    def first_common(self):
        print('I am first common...')

    def second_common(self):
        print('I am second common...')

    @abstractmethod
    def third_require(self):
        pass

    @abstractmethod
    def fourth_require(self):
        pass

    def hook(self):
        pass


class One(Top):
    def third_require(self):
        print('I am third require from One...')

    def fourth_require(self):
        print('I am fourth require from One...')

    def hook(self):
        print('I am Hook from One...')


class Two(Top):
    def third_require(self):
        print('I am third require from Two...')

    def fourth_require(self):
        print('I am fourth require from Two...')


def client(class_):
    class_().template_method()


if __name__ == '__main__':
    client(One)
    client(Two)
