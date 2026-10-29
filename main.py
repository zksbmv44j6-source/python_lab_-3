def greet(name):
    print("Здравствуйте,", name)


def square(number):
    return number ** 2


def max_of_two(a, b):
    if a > b:
        return a
    return b
greet("Анна")
greet("Иван")

print("Квадрат числа 4 =", square(4))
print("Квадрат числа 7 =", square(7))

print("Большее из 5 и 9:", max_of_two(5, 9))
print("Большее из 12 и 3:", max_of_two(12, 3))


