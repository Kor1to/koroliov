#первое дз

def cash (min_cash):
    for el in min_cash:
        if el <= 500:
            bonus = el + 100
            print("Зарплата: " + str(bonus) + " $")

        else:
            print("вы и так получаете кучу денег")


sasha = [800]
cash(sasha)

den = [600]
cash(den)

renat = [200]
cash(renat)

tolia = [500]
cash(tolia)





#####
file = open('data/text.txt', 'a')
x = 0
while x == 0:
    try:
        y = input("Как вас зовут?")
        x = int(input("Какая у вас зарплата?"))

        if x < 100:
            price = x + 100
            print("УУУ "+ y + " вы получаете мало денег. Вот вам бонус! + 100$ теперь ваша зарплата:" + str( price ) + "$")
            file.write( y + " получает: " + str(price) + "\n")
        else:
            print("Поздравляем вы на хорошем уровне")
            file.write( y + " получает: " + str(x) + "\n")
    except ValueError:
        print("Введите пожалуйста зарплату в цыфрах")

print("Зарплата всех друзей:")

file = open('data/text.txt', 'r')

for line in file:
    print(line, end="")

file.close()


