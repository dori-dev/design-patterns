from __future__ import annotations


class State:
    def __init__(self, tv: TV):
        self.tv = tv
        self.status = None

    def operate(self):
        print(f'Turning TV {self.status}')


class TurnOn(State):
    def __init__(self, tv):
        super().__init__(tv)
        self.status = 'On'

    def change_state(self):
        print('Changing state to On...')
        self.tv.state = self.tv.off


class TurnOff(State):
    def __init__(self, tv):
        super().__init__(tv)
        self.status = 'Off'

    def change_state(self):
        print('Changing state to Off...')
        self.tv.state = self.tv.on


class TV:
    def __init__(self):
        self.on = TurnOn(self)
        self.off = TurnOff(self)
        self.state = self.on

    def press(self):
        self.state.operate()
        self.state.change_state()


if __name__ == '__main__':
    tv = TV()
    tv.press()
    tv.press()
    tv.press()
