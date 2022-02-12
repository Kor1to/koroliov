# списки количиство бесконечно
# скобки обезательно [] можно хранить разные типы данных
# вытаскивает чиисла даже из второго списка

nums = [5, 5,3,6,7,8, True,"Hello", [6,4]]

nums[0] = 50
nums [6] = False


print(nums[-1][1])
# append добавляет элемент в строку в конец
# insert два параметра заменяет п
# extend добавляет в конец смешает
# #sort все элементы отсортированы
# reverse переворачивает строчку
# pop если ничего не писать последний элемент удаляется( можно ()по индексу)
# remove ( что удалить ) то и удаляет
# clear полностью чистит
# count считает количиство совпадений элементов (.count (".. ")
# len размер длиина списка



numbers = [5, 2, 4]

numbers.append(100)
numbers.insert(1, True)
numbers.extend([9, 7])
numbers.sort()

print(numbers)

# for удобен для перебора строк
nums = [5, 3,4,5, "eoe", False]
for el in nums:
    print(el)



# программка добавления чисел
n = int(input("введите длину списка:"))

user_list = []
i = 0
while i < n:
    string = "Ввидите элемент #" + str(i+1) + ": "
    user_list.append(input(string))
    i += 1

print(user_list)


# строки
# split что бы разбить строку на отдельные слова (.split('символ которые разьмвает строку'))
#

word = "fotbal, basketbol, skate"

hobby = word.split(', ')

print(hobby[1])

#программа обрашение к каждому элемента списка и capitalise


for i in range(len(hobby)):
    hobby [i] = hobby[i].capitalize()
resultl = ", ".join(hobby)
print(resultl)

# индексы и срезы

word =" футбол"
print(word[0:3:])