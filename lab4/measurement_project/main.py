import json
import logging
from pathlib import Path

from utils.reader import read_numbers, validate_numbers
from utils.statistics import calculate_average, find_min, find_max


def main():
    with open("config.json", "r", encoding="utf-8") as file:
        config = json.load(file)

    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    logging.basicConfig(
        filename=config["log_file"],
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        encoding="utf-8",
    )
    logging.info("Программа запущена")

    print("Рабочий каталог:", Path.cwd())

    input_file = Path(config["input_file"])
    print("Путь к файлу:", input_file)
    print("Файл существует:", input_file.exists())

    try:
        numbers = read_numbers(input_file)
        validate_numbers(numbers)
    except FileNotFoundError:
        print("Файл не найден")
        logging.error(f"Файл не найден: {input_file}")
    except ValueError as error:
        print("Ошибка в данных:", error)
        logging.error(f"Некорректные данные: {error}")
    else:
        logging.info(f"Файл прочитан: {input_file}")
        logging.info(f"Прочитано значений: {len(numbers)}")
        print("Количество значений:", len(numbers))
        print("Минимум:", find_min(numbers))
        print("Максимум:", find_max(numbers))
        print("Среднее:", calculate_average(numbers))
    finally:
        logging.info("Программа завершена")


if __name__ == "__main__":
    main()