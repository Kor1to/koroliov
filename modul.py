### модули сешетвует множество как встроеные так и от других разработчиков

### пишется import
### time работает с временем
# программа котрая делает задержку сообщения
import platform
import time

time.sleep(1)
print("Hello")

### datetime модно работать с датой и временем
### import datetime as d ---- можно сократить написание полного модуля на одну букву
import datetime as d
print(d.datetime.now().time())

### информация про пользователя  sys, os
# можно прописывать несколько модулей в строку

import datetime as d, sys, os
print(d.datetime.now())
print(sys.path) # путь к тикушему файлу
print(os.name) #
print(platform.system()) ### рабочее название системы

#random рандомное число
# aray с масивами
# math математические функции

## можно указывать что именно мы импортируем из модуля
## from
from math import sqrt as s, ceil
print(ceil(s(25)))

import mymodul as my
print(my.name)
my.hello()

###
from mymodul import ###можно импортировать не все модули а по отдельности
