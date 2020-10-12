# Задача «Переставить min и max»
# Условие
# В списке все элементы различны. Поменяйте местами минимальный и
# максимальный элемент этого списка. \

li = [int(i) for i in input().split()]
min_i, max_i = 0, 0
for i in range(0, len(li)):
    if li[i] < li[min_i]: min_i = i
    if li[i] > li[max_i]: max_i = i
li[min_i], li[max_i] = li[max_i], li[min_i]
print(' '.join([str(i) for i in li]))