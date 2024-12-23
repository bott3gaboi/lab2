def describe_person(name, age=30):
    print("Имя:", name + ", возраст:", age)


name = input("Введите имя: ")
age = input("Введите возраст: ")
if age == "":
    describe_person(name)
else:
    describe_person(name, int(age))