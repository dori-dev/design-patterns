class Singleton(type):
    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__(*args, **kwargs)
        return self._instance


class DB(metaclass=Singleton):
    pass


if __name__ == '__main__':
    d1 = DB()
    d2 = DB()
    print(d1 is d2)
