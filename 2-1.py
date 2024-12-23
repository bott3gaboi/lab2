def greet(name):
    print("Привет,", name)


def square(number):
    print(number**2)


def max_of_two(x, y):
    print(max(x, y))


greet(input("Введите имя: "))
square(int(input("Введите число: ")))
max_of_two(int(input("Введите первое число: ")), int(input("Введите второе число: ")))