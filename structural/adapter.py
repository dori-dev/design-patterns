class Socket:
    _type = None


class SocketA(Socket):
    _type = '2'


class SocketB(Socket):
    _type = '1'


class Adapter:
    _socket: Socket = None
    _pin_type = None

    def __init__(self, socket):
        self._socket = socket


class AdapterA(Adapter):
    _socket: Socket = None
    _pin_type = '3To2'


class AdapterB(Adapter):
    _socket: Socket = None
    _pin_type = '3To1'


class Fridge:
    _adaptor: Adapter = None
    _pin_type = '3'

    def __init__(self, adapter):
        self._adaptor = adapter

    def freeze(self):
        if self._adaptor._pin_type == (
            self._pin_type + 'To' + self._adaptor._socket._type
        ):
            print('Done!')
        else:
            print('Sorry, Not Usable!')


if __name__ == '__main__':
    socket1 = SocketA()
    adapter1 = AdapterA(socket1)
    fridge1 = Fridge(adapter1)
    fridge1.freeze()

    socket2 = SocketB()
    adapter2 = AdapterA(socket2)
    fridge2 = Fridge(adapter2)
    fridge2.freeze()

    socket3 = SocketB()
    adapter3 = AdapterB(socket3)
    fridge3 = Fridge(adapter3)
    fridge3.freeze()
