from test import *


def print_hi(name):
    print(f'Hi, {name}')


# def print_hi(name="Pycharm"):  # Значение функции по умолчанию
#     print(f'Hi, {name}')


def print_worker(name, age, company):
    print(f"Name: {name}")
    print(f"age: {age}")
    print(f"Company: {company}")


# def print_worker(name, age, company="Apple"): #Если несколько параметров то необязательные после обязятальных
#     print(f"Name: {name}")
#     print(f"age: {age}")
#     print(f"Company: {company}")

# Символ *, какие параметры будут именнованные
# параметры справа от * получаеют значения только по имени
def print_worker(name, *, age, company):
    print(f"Name: {name}")
    print(f"age: {age}")
    print(f"Company: {company}")


# Можно сделать позиционные параметры, используя символ /
# Все параметры до / являются позиционными
def print_worker(name, /, age, company="Dota 2"):
    print(f"Name: {name}")
    print(f"age: {age}")
    print(f"Company: {company}")


# Можно определять позиционные и именные параметры

# Неопределенное количество параметром с помощью *
# def summa(*numbers):
#     res = 0
#     for i in numbers:
#         res += i
#     print( f'Sum = {res}')


if __name__ == '__main__':
    print_hi("PyCharm")


    # print_worker("Tom", 37, "Google")
    # print_worker(age=45, name="Pudge", company="Dota 2")
    # print_worker("Zeus", age=18, company="Dota2")
    #print_worker("Invoker", age=555)
    # summa(1, 3, 5, 6)
    # summa(1, 4, 6)
