# 2. Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывести в консоль сам список и сумму его элементов.


n = int(input('Введите число N: '))

# my_list = []                           # Было так
# summ = 0
# # for i in range (1,n+1):
# #     my_list.append((1+1/i)**i)
# #     summ += my_list[i-1]

my_list  = list(map(lambda i: (1+1/i)**i, [i for i in range (1,n+1) ]))
print(*my_list, sep=', ')

summ = sum(my_list)

print(f'Сумма элементов равна {summ}')