class Raw:
    def raw(self):
        print('Buying raw foods from market...')


class Transfer:
    def transfer(self):
        print('Transferring raw foods to restaurant...')


class Cook:
    def cook(self):
        print('Cooking raw foods by chief...')


class Serve:
    def serve(self):
        print('Serving food to client...')


class ItalianRestaurant:
    def get(self):
        r = Raw()
        r.raw()
        t = Transfer()
        t.transfer()
        c = Cook()
        c.cook()
        s = Serve()
        s.serve()


def order():
    italian_food = ItalianRestaurant()
    italian_food.get()


if __name__ == '__main__':
    order()
