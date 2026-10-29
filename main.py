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

value = 10

def example():
    
    value = 20
    print("Внутри функции:", value)

example()
print("Снаружи функции:", value)
def another_example():
    local_var = 42
    print("Внутри функции:", local_var)

another_example()

# print(local_var)

numbers = [15, 8, 23, 42, 4, 16, 9, 31, 7, 50]

print("Первый элемент:", numbers[0])
print("Третий элемент:", numbers[2])
print("Последний элемент:", numbers[-1])

numbers[1] = 100
print("После изменения второго элемента:", numbers)

numbers.append(77)
print("После append(77):", numbers)

numbers.remove(42)
print("После remove(42):", numbers)


print("Итоговый список:", numbers)
print("Количество элементов:", len(numbers))


