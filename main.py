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

def calculate_rectangle(width, height):
    return width * height
area = calculate_rectangle(10, 5)
print("Площадь прямоугольника 10 на 5 равна:", area)

def calculate_perimeter(width, height):
    return 2 * (width + height)

perimeter = calculate_perimeter(10, 5)
print("Периметр прямоугольника 10 на 5 равен:", perimeter)

def describe_rectangle(width, height, unit="см"):
    print(f"Прямоугольник: ширина {width} {unit}, высота {height} {unit}")
describe_rectangle(10, 5)
describe_rectangle(20, 15, "дюймов")


