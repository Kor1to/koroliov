# tuple кортеж константа значения не изменяются
# похожи со списками
# меньше памяти занимают
# испольщуются для передачи данных
# для созлания круглые скобки ()
# кортежи нет разных функций count количество найденых элимента
# len длина всего картежа

data = (3,4,5,6,2, True,"hello")

print (len(data[1:3]))


# можно создавать без скобок

data = 1,45 ,"dat"
print(data)

#изменить список в картеж

nums = [2, 5, 6]
new_data = tuple(nums)
print(new_data)

word = tuple("Hello world")
print(word)


#  Словари

person =\
{"user_1":
    { "first_name" : "Anatoli",
      "last_name" : "Koroliov",
      "age" : "25",
      "strit" : ("Moldova","Comrat","Lenina","157"),
    }
}
{"user_2":
     {"first_name" : "vika"
     }
}

print(person ["user_1"]["strit"][1:5])


######

code = { "marka": "iphone", "model": "10", "problem": "touch"}

for key, value in code.items():
    print(key, ":", value )