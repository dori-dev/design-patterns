from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractHandler(ABC):
    def __init__(self, successor):
        self._successor: AbstractHandler = successor

    def handle(self, request):
        handled = self.process_request(request)
        if handled is None:
            self._successor.handle(request)

    @abstractmethod
    def process_request(self, request):
        pass


class HandlerOne(AbstractHandler):
    def process_request(self, request):
        if 0 < request <= 10:
            print(f'Handler One is processing this request({request})')
            return True


class HandlerTwo(AbstractHandler):
    def process_request(self, request):
        if 10 < request <= 20:
            print(f'Handler Two is processing this request({request})')
            return True


class HandlerThree(AbstractHandler):
    def process_request(self, request):
        if 20 < request <= 30:
            print(f'Handler Three is processing this request({request})')
            return True


class DefaultHandler(AbstractHandler):
    def process_request(self, request):
        print(f'Default handler is processing this request({request})')
        return True


class Client:
    def __init__(self):
        self.handler = HandlerOne(
            HandlerTwo(
                HandlerThree(
                    DefaultHandler(None)
                )
            )
        )

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)


if __name__ == '__main__':
    requests = [3, 14, 30, 50, 100, 2, 23, 12, 31]
    client = Client()
    client.delegate(requests)
