from pathlib import Path

from utils.reader import read_numbers, validate_numbers
from utils.statistics import calculate_average, find_min, find_max


def main():
    print("Рабочий каталог:", Path.cwd())

    input_file = Path("data") / "measurements.txt"
    print("Путь к файлу:", input_file)
    print("Файл существует:", input_file.exists())

    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    try:
        numbers = read_numbers(input_file)
        validate_numbers(numbers)
    except FileNotFoundError:
        print("Файл не найден")
        return
    except ValueError as error:
        print("Ошибка в данных:", error)
        return

    print("Количество значений:", len(numbers))
    print("Минимум:", find_min(numbers))
    print("Максимум:", find_max(numbers))
    print("Среднее:", calculate_average(numbers))


if __name__ == "__main__":
    main()