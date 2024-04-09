import time

def SimpleNumbers(min_num: int, max_num: int) -> [int]:
    """
    Решето Эратосфена
    """
    start_time = time.time()

    # Если пользователь ввел минимальное число или максимальное число меньше 2,
    # то устанавливаем его принудительно на дефолтное значение 2
    min_num = min_num if min_num >= 2 else 2
    max_num = max_num if max_num >= 2 else 2

    a = list(range(min_num, max_num + 1))
    data = []

    i = min_num
    while i <= max_num:
        if a[i - min_num] != 0:
            if i >= min_num:
                data.append(a[i - min_num])
            for j in range(i, max_num + 1, i):
                a[j - min_num] = 0
        i += 1

    spread = time.time() - start_time
    return data, spread


def main():
    while True:
        try:
            min_range = int(input('Введите минимальное значение (от 2 и более): '))
            max_range = int(input('Введите максимальное значение: (от 2 и более): '))
            new_list, spread = SimpleNumbers(min_range, max_range)
            print(f'Список простых чисел: {new_list}')
            print(f'Время выполнения: {spread} секунд')
            break
        except ValueError:
            print("Введите целое число!")


if __name__ == '__main__':
    main()

