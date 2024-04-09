
def sort_by_length(strings):
    sorted_strings = sorted(strings, key=len)
    return sorted_strings


def main():
    strings = ["python", "fastapi", "django", "vue.js", "flask", "postgresql", "redis", "aiohttp", "git", "celery", "docker", "rabbitmq"]
    sorted_strings_asc = sort_by_length(strings)
    print("Сортировка по длине строки в порядке возрастания:", sorted_strings_asc)

    sorted_strings_desc = sorted(strings, key=len, reverse=True)
    print("Сортировка по длине строки в порядке убывания:", sorted_strings_desc)


if __name__ == '__main__':
    main()

