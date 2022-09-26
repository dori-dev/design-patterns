class Iteration:
    def __init__(self, value):
        self.value = value

    def __next__(self):
        if self.value == 0:
            raise StopIteration('End of sequence...')
        for _ in range(self.value):
            value = self.value
            self.value -= 1
            return value

    def __iter__(self):
        return self


class Iterable:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return Iteration(self.value)


if __name__ == '__main__':
    numbers = Iterable(20)
    for number in numbers:
        print(number)
