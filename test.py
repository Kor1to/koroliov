
class Frends:
    name = None
    age = None
    price = None

    def __init__(self, name, age, price):
        self.set_data(name, age, price)
        self.get_data()

    def set_data(self, name, age, price):...

    def get_data(self):
        print()

tolia = Frends('Толя', 25, 1050)


sasha = Frends('Саша', 30, 50)