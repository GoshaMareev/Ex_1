def print_test(): print("Test Works")


def print_test2():
   #Локальные функции
    def hello(): print("Hello")

    def world(): print("World")

    hello()
    world()
