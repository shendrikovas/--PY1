list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
i = 0
max_ = list_numbers[i]

for ord, num in enumerate(list_numbers):
    if num > max_:
        max_ = num
        i = ord

list_numbers[i], list_numbers[-1] = list_numbers[-1], list_numbers[i]

# TODO Оформить решение

print(list_numbers)
