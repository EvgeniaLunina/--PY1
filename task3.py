import random
size = 15

def get_unique_list_numbers() -> list[int]:
    unique_set = set()
    while len(unique_set) != size:
        unique_set.add(random.randint(-10, 10))
    unique_list = list(unique_set)
    return unique_list

    ...  # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
