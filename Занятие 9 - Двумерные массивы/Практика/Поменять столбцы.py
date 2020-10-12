# Задача «Поменять столбцы»
# Условие
#
# Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j
# и выведите результат.
#
# Программа получает на вход размеры массива n и m, затем элементы массива, затем числа
# i и j.
#
# Решение оформите в виде функции swap_columns(a, i, j).

def swap_columns(a, i, j):
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i]
    return a

n, m = map(int, input().split())
db = [list(map(str, input().split())) for _ in range(n)]
i, j = map(int, input().split())

print(*[' '.join(z) for z in swap_columns(db, i, j)], sep='\n')
# print(*[' '.join(i) for i in swap_columns(db, i, j)], sep='\n')