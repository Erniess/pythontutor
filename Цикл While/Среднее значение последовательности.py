# Задача «Среднее значение последовательности»
# Условие
# Определите среднее значение всех элементов последовательности, завершающейся числом 0.

length = 0
summ = 0
n = int(input())
while n != 0:
    summ += n
    length += 1
    n = int(input())
print(summ / length)