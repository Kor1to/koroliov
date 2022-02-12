
# прописываем open( адрес 'data/text.txt', 'w') чтение
# закрываем file.close()
# w стирает и записывает новую
# а к текушей добавляет информации


file = open('data/text.txt', 'w')

file.write("Den")

file.close()



data = input("введите вашу зарплату")

file = open('data/text1.txt', 'a')

file.write(data + "\n")

file.close()


file_1 = open('data/text1.txt', 'r')
#print(file_1.read()) #в скобках пишик количество символов

# если нужно выводить по строчкам пишем функцию
for line in file_1:
    print(line, end="")
# end="" убираем перенос строки

file_1.close()


#### менеджер with as он открывает и чуть позже сам закрывает файл

try:
    with open('data/text.txt', 'r', encoding='utf-8') as file:
         print(file.read())
except FileNotFoundError:
    print("Файл не был найден")


