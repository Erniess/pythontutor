# Задача «Сумма десяти чисел»
# Условие
# Дано 10 целых чисел. Вычислите их сумму. Напишите программу, использующую
# наименьшее число переменных.

print(sum([int(input()) for _ in range(10)]))