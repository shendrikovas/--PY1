# TODO написать функцию для получения списка уникальных целых чиселimport random
import random

def get_unique_list_numbers() -> list[int]:
    num = 15
    list_ = [random.randint(-10, 10) for x in range(num)]
    list_unique = set(list_)
    while len(list_unique) < num:
        list_ = list_ + [random.randint(-10, 10) for x in range(num - len(list_unique))]
        list_unique = set(list_)
    list_ = [numb for numb in list_unique]
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

