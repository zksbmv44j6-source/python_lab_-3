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

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

def find_min(numbers):
    minimum = numbers[0]  
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

test_numbers = [5, 2, 9, 1, 7]

print("Своя сумма:", calculate_sum(test_numbers), "| Встроенная sum:", sum(test_numbers))
print("Свой минимум:", find_min(test_numbers), "| Встроенная min:", min(test_numbers))
print("Свой максимум:", find_max(test_numbers), "| Встроенная max:", max(test_numbers)) 
 
def find_element(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i 
    return -1  

test_list = [10, 20, 30, 40, 50]
print("Индекс 30:", find_element(test_list, 30))  

print("Индекс 99:", find_element(test_list, 99)) 

def analyze(numbers):
    minimum = find_min(numbers)
    maximum = find_max(numbers)
    average = calculate_sum(numbers) / len(numbers)
    return minimum, maximum, average  

test_data = [10, 20, 30, 40, 50]
min_val, max_val, avg_val = analyze(test_data)

print("Минимум:", min_val)
print("Максимум:", max_val)
print("Среднее:", avg_val)

numbers = [-10, 3, -2, 8, -5]

normal_sorted = sorted(numbers)
print("Обычная сортировка:", normal_sorted)  

abs_sorted = sorted(numbers, key=lambda x: abs(x))
print("Сортировка по модулю:", abs_sorted) 

def calculate_average(measurements):
    total = 0
    for m in measurements:
        total += m 
    return total / len(measurements)

def find_minimum(measurements):
    minimum = measurements[0]
    for m in measurements:
        if m < minimum:
            minimum = m
    return minimum

def find_maximum(measurements):
    maximum = measurements[0]
    for m in measurements:
        if m > maximum:
            maximum = m
    return maximum

def count_above_average(measurements):
    avg = calculate_average(measurements)
    count = 0
    for m in measurements:
        if m > avg:
            count += 1
    return count

def find_value(measurements, target):
    for i in range(len(measurements)):
        if measurements[i] == target:
            return i
    return -1

def analyze_measurements(measurements):
    return find_minimum(measurements), find_maximum(measurements), calculate_average(measurements)

measurements = [12.5, 18.3, 7.1, 22.8, 15.0, 9.9, 30.2, 11.4, 25.6, 13.7, 19.1, 8.8]

print("=== АНАЛИЗ ИЗМЕРЕНИЙ ===")
print("Количество измерений:", len(measurements))
