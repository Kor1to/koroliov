

class Building:
    year = None
    city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city
       #self.get_info()

    def get_info(self):
        print("Возраст:", self.year, "Город:", self.city)

### можно создать дополнительно под поля которое насленует все параметры родителя
class School(Building): ## один класс только один родитель
    pupils = 0

    def __init__(self, pupils, year, city):
        super(School, self).__init__(year, city) ### super вызывает родительский
        self.pupils = pupils

    def get_info(self): #### полиморфизм можно переписать метод
        super().get_info()
        print("Ученики",self.pupils)

###класс наследник может содержать еще наследники


school = School(1900, 11, "Comrat")
school.get_info()
house = Building(1900, "Comrat")
cildren = Building(1900, "Comrat")
shop = Building(1900, "Comrat")


### инкапсуляции любые поля должны быть зашишеные
# достук к полян должен быть через другие поля
# __ два нижних подчеркивания пишется для того что бы нельзя было выводить данные