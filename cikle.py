# цыклы
# for когда нужно что то перребрать. диапозон
# while просто прописать условие когда просто прописать и продолжить \
# 1 параметр в скобках от
# 2 параметр до
# 3 параметр шаг
#    for i in range(1, 6, 2):
#         print(i)

count = 0
word = "hello"
for i in word:
    if i =="l":
        count += 1

print("Count:", count)

#цикл while разница в формате записи. можно просто указать условие

f = 5
while f < 15:
    print(f)
    f += 2
# while просто прописать условие когда просто прописать и продолжить \

isHasCar = True

while isHasCar:
    if input("ввидите даныне") == "stop":
        isHasCar = False

#выйти из цыкла break
for i in range (1, 11):
    if i == 5:
        break
# continue пропускает ее а не останавливает
# None в самом начале ничего не прописываем

# программа поиска
found = None
for i in "Hello":
    if i == "l":
        found = True
        break
else:
    found = False

print(found)
