# В массиве целых чисел с количеством элементов 19 определить
# максимальное число и заменить им все четные по значению элементы.

numbers = [12, 3, 56, 645, -76, 435, 3, 678, 1000, 34, 563, 11, 13, 90, 45, 4234, 2556576, 6, 1]

i = 1
while i < 19:
    numbers[i] = max(numbers)
    i += 2

print(numbers)
