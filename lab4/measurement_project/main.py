from utils.statistics import calculate_average, find_min, find_max


def main():
    numbers = [42, 38, 51, 35, 57]
    print("Среднее:", calculate_average(numbers))
    print("Минимум:", find_min(numbers))
    print("Максимум:", find_max(numbers))


if __name__ == "__main__":
    main()