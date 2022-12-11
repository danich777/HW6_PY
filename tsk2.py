# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

num = input('Введите число: ')

# summ = 0
#
# for digit in num:
#     if digit.isdigit():
#         summ += int(digit)

num = num.replace(',', '')
new_num = map(int, num)
summ = sum(new_num)
print(summ)