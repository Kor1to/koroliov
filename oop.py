### ООП  обший класс позволяет сократить код
class Frends:
    name = None
    age = None
    IsHappy = None
    price = None

    def set_data(self, name, age, price):
        self.name = name   ## self ставиться для того что бы взять превый параметр из класса
        self.age = age
        self.price = price

    def get_data(self):  ##названия функций может быть разное
        print("Имя:", self.name, "Возраст:", self.age, "Зарплата", self.price, "$")



tolia = Frends()### в скобках пишется список обьектов когда есть конструктор
tolia.set_data("Толя", 25, 1000) ### метод через функцию можно писать параметры в одну строку
#tolia.name = 'Толя' ## Можно так прописывать отдельно
#tolia.price = "1000"

sasha = Frends()
sasha.name = 'Саша'
sasha.price = "500"

print(tolia.price)
print(tolia.name)

tolia.get_data()
sasha.get_data()

### Конструкторы классов,
# можно выполнить код сразу при введение
# def __init__
#         pass
# так создается конструктор

class Frends1:
    name = None
    age = None
    IsHappy = None
    price = None

    def __init__(self, name = "Дружок", age = None , price = None):#### конструктор
        self.set_data(name,age,price)
        self.get_data()

    def set_data(self, name, age, price):
        self.name = name
        self.age = age
        self.price = price

    def get_data(self):
        print("####")
        print("Имя:", self.name, "Возраст:", self.age, "Зарплата", self.price, "$")

tolia = Frends1('Толя', 25, 1050)

Denis = Frends1()

sasha = Frends1('Саша', 30, 50)


### Переопределения методов устанавливать значения по умолчанию
#   def set_data(self, name = None, age = None, price = None):
###   тоже можно вывести идля конструктора
#   def __init__(self, name = "Дружок", age = None , price = None):
