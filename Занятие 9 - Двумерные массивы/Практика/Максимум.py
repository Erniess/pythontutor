# Задача «Максимум»
# Условие
#
# Найдите индексы первого вхождения максимального элемента. Выведите два числа:
# номер строки и номер столбца, в которых стоит наибольший элемент в двумерном массиве.
#  Если таких элементов несколько, то выводится тот, у которого меньше номер строки,
# а если номера строк равны то тот, у которого меньше номер столбца.
#
# Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой.

n, m = map(int, input().split())
db = [list(map(int, input().split())) for _ in range(n)]

coord = [0, 0]
for i in range(n):
    for k in range(0, m):
        if db[i][k] > db[coord[0]][coord[1]]:
            coord = [i, k]
print(coord[0], coord[1], sep=' ')