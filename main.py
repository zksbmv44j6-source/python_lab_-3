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

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Первые три:", numbers[:3])

print("Последние три:", numbers[-3:])

print("С 3-го по 7-й:", numbers[2:7])

print("Каждый второй:", numbers[::2])

print("Обратный порядок:", numbers[::-1])

measurements = (12.5, 18.3, 7.1, 22.8, 15.0, 9.9, 30.2, 11.4)

print("Первый:", measurements[0])
print("Последний:", measurements[-1])

print("Срез [1:4]:", measurements[1:4])

#measurements[0] = 99

first, second = measurements[0], measurements[1]
print("Первое значение:", first)
print("Второе значение:", second)

temp_list = list(measurements)
print("Список:", temp_list)

temp_list[0] = 99
print("Изменённый список:", temp_list)

new_measurements = tuple(temp_list)
print("Новый кортеж:", new_measurements)
# Используем тот же список numbers из задания 4
numbers = [15, 100, 23, 4, 16, 9, 31, 7, 50, 77]  # (без 42, с 100 и 77)

print("Количество:", len(numbers))
print("Сумма:", sum(numbers))
print("Минимум:", min(numbers))
print("Максимум:", max(numbers))

# Среднее = сумма / количество
average = sum(numbers) / len(numbers)
print("Среднее:", average)

# sorted() возвращает новый отсортированный список (исходный не меняется)
sorted_copy = sorted(numbers)
print("Отсортированная копия (sorted):", sorted_copy)
print("Исходный список после sorted:", numbers)  # не изменился!

# sort() изменяет сам список
numbers.sort()
print("После sort() исходный список:", numbers)