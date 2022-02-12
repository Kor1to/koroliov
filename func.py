#   функции
# PASS Ничего выполнять не буду
# end=""перехода на новую строку не буду
# в скобках пигется парамет или переменные (Word) можно мередавать сколько угодно,
#


def test_func (word):
    print(word, end="")
    print("!")

test_func("Hi")



def suma(a, b):
    res = a + b
    print("result", res)

suma(5,5)
suma("H", "I")

# что бы использовать значение после выполнения функции использовать return
def suma(a, b):
    res = a + b
    return res

res = suma(5,10)
print(res)

#
#
# программа нахождения минимального значения

nums_1 = [5, 6, 8, 9]

min = nums_1[0] #показваем минимальный элемент
for el in nums_1: # цыкл перебираем nums1
    if el < min:  # (условие) если элемент меньше
        min = el  # меняем значение минимального элемента

print(min)


nums_2 = [5.1,5.5, 6.1, 6.6, 8, 9]

min2 = nums_2[0] #показваем минимальный элемент
for el in nums_2: # цыкл перебираем nums1
    if el < min2:  # (условие) если элемент меньше
        min2 = el  # меняем значение минимального элемента

print(min2)

# можно так но можно прописать фукцию и строчек кода будет меньше

def minimal(l):
    min_number = l[0]
    for el in l:
        if el < min_number:
            min_number = el

#либо просто print(min_number)
    return min_number   #либо возврашать

nums_3 = [5, 6, 8, 9, 2]
min1 = minimal(nums_3)


nums_4 = [5, 5.5, 6.1, 6.6, 8, 9, 3.1]
min2 = minimal(nums_4)

if min1 < min2:
    print(min1)
else:
    print(min2)


#ананимные функции lambda после : пишится то что нужно сделать
fun = lambda x, y : x-y
fun = fun(4, 20)
print(fun)