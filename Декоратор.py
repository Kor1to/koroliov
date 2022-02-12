import webbrowser ## встроеный модуль

def validator(func):
    def wrapper(url):
        print("Текст до функции")
        func(url)
        print("Текст после функции")
    return wrapper

@validator
def open_url(url): ##открывает ссылку
    webbrowser.open(url)

open_url("https://jw.org")

########

import webbrowser

def validator(func): #выполняем проверку до выполнение функции
    def wrapper(url):
        if "." in url:
            func(url)
        else:
            print("неверный URL")
    return wrapper

@validator### декоратор котрый добавляет действие
def open_url(url): ##открывает ссылку
    webbrowser.open(url)

open_url("https://jworg")

### можно добавлять сколько угодно для добавления функционала и проверки