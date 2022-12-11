# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

size = int(input('Введите размер списка: '))
my_list = [randint(0, 10) for i in range(size)]

# my_list = []
#
# for i in range (size):
#     my_list.append(rnd(0,10))

print(my_list)
odd_numbers = list(v for i, v in enumerate(my_list) if i % 2)
print(f'Элементы с нечетными индексами {odd_numbers}')
print(F'Ответ {sum(odd_numbers)}')

# summ = 0
# for i in range (1, size, 2):
#     summ += my_list[i]
# print(summ)