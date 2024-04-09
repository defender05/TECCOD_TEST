
def task_01(int_list: [int]) -> [int]:
    """
    Функция принимает список целых чисел и возвращает новый список целых чисел без дубликатов.
    """
    return set(int_list)


if __name__ == '__main__':
    new_list = task_01([1, 1, 2, 3, 5, 8, 5, 21, 3, 55, 89])
    print(new_list)

