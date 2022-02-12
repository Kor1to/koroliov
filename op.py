# условные операторы

# важно растояние пробелов (отступы) в if
user_data = int(input("Введите число"))
if user_data != 5:
    print("Мы на месте")
    if user_data > 6:
        print("Больше 6")

#
#
isHappy = True

if isHappy or user_data == 6:
    print("Пользователь счастлив")
elif user_data == 5:
    print("Номер равен 5")
elif user_data == 7:
    print("Номер равен 7")
else:
    print("Пользователь не счастлив")
# else  в самом конце. сработает если if не сработал. используется с if
# elif пишится между else и if

# оператор and оба должны быть правильными
# оператор or [хотябы один оператор положительный


data = input()

if data == "Five":
    number = 5
else:
    number = 0
print(number)

# тирнальный оператор
number = 5 if data == "Five" else 0
# тоже самое только в одной строке. можно использовать если нужен только if и else




