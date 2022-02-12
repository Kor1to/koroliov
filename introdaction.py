# функции
#sep="" разделитель функция прописывается в конце
#end= "" функция для конца строки/ если значение пустое он не переносит на новую строку
#\n : с новой строки [с новой строки]
#\t табуляция растояние от строки
# min функция найдет минимальный элемент
# max функция найдет максимальное значение
# round округляет число к ближайшему
# input ("введите:") получать значения "" можно парпметр получичать


# ПЕРЕМЕНЫЕ название могут называться как удобно
# bool либо истна true либо лож folse {bolean = True}
# разныет типы данных сложение невозможно к строке другой нельзя либо через запятоц либо str(другие данные)
# str -строки. int - целые числа. float- дробные числа. bool- истина или лож
#
#


num1= int(input("Введите первое число:"))

num2= int(input("Введите второе число"))

print("Результат:", num1 + num2)
print("Результат:", num1 - num2)
print("Результат:", num1 / num2)
print("Результат:", num1 * num2)

# конструкции if токсть если. прини выводит только если значение верное
if 5 > 5:
    print("Yes")
    print("!!!")

# важно растояние пробелов (отступы) в if
user_data = int(input("Введите число"))
if user_data != 5:
    print("Мы на месте")
    if user_data > 6:
        print("Больше 6")




model_car = "BMW"
color_car = "blu"
year = 2004
number_of_doors = 5

print(model_car)
print(color_car)
print(year)
print(number_of_doors)


#вычисления возраста

age_1 = 20
age_2 = 25
age_3 = 40
age_4 = 28
age_5 = 30
number_people = 5
average = ( age_1 + age_2 + age_3 + age_4 + age_5 / number_people )

print(average)
print("______")


#строки

name = "Maikl"
first_name = "Konor"
age = "25"
space = " "
text = "Hi! My name is" + space + name + space + first_name + ", I'm " + age + space + "years old."

print(text)


muzic = """"
\t\tBaa, baa, black sheep,
\t\tHave you any wool?
\t\tYes sir, yes sir,
\t\tThree bags full

\t\tOne for the master,
\t\tOne for the dame,
\t\tAnd one for the little boy
\t\tWho lives down the lane

\t\tBaa, baa, black sheep,
\t\tHave you any wool?
\t\tYes sir, yes sir,
\t\tThree bags full
"""
print(muzic)

text_muzic = " \n\t\t Baa, baa, black sheep,\
\n\t\t Have you any wool?\
\n\t\t Yes sir, yes sir,\
\n\t\t Three bags full\n \
\n\t\t One for the master,\
\n\t\t One for the dame,\
\n\t\t And one for the little boy\
\n\t\t Who lives down the lane \n \
\n\t\t Baa, baa, black sheep, \
\n\t\t Have you any wool? \
\n\t\t Yes sir, yes sir, \
\n\t\t Three bags full\
"

print(text_muzic)


##
greeting = "Привет"
print(greeting[::-1])
#len - индкс в строке "количиство символов"
#[] - в скобках выводит символ [писать цыврами с 0 ]
#[1:5] - slicing кусок строки символ не включая его до него
#[9::3] -9:с какого символа начинать/ 3 :указываем шаг наприме 3
#[::-1] Переворачивает символы


#вывести слово path
greeting_hel = "Hello Python"
path = ( greeting_hel[6] + "a" + greeting_hel[8:10] )
print(path)
print("11111"+"\n")
#форматирование строк .format

float_resalt = 2000 / 7
print(float_resalt)
print("результат: {0:1.4f} ".format(float_resalt))

name = "mark"
age = "25"
name_and_age = "my name is {0}. I m {1} yer old" .format( name, age)
print(name_and_age)


week_day = "wek day: {gu} and {mo}" .format( gu='erv', mo='fmfm')
print(week_day)

print('''
 {0:15.4f} {1:15.4f} {2:15.4f} {3:15.4f} 
 {4:15.4f} {5:15.4f} {6:15.4f} {7:15.4f}
'''.format( 1.12345, 1.23456, 1.34567, 1.456789, 1.567890, 1.6789, 1.7890,1.89098))


table = f"""{1.23456:15.4f}{78.901234:15.4f}{567.8901234:15.4f}{5678.90123456:15.4f}
{567.8901234:15.4f}{1.23456:15.4f}{5678.90123456:15.4f}{78.901234:15.4f}"""
print(table)

