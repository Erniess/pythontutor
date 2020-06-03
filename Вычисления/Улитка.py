# Задача «Улитка»
# Условие
#
# Улитка ползет по вертикальному шесту высотой h
# метров, поднимаясь за день на a метров, а за ночь спускаясь на b
#
# метров. На какой день улитка доползет до вершины шеста?
#
# Программа получает на вход натуральные числа h
# , a, b
#
# .
#
# Программа должна вывести одно натуральное число. Гарантируется, что a>b
# .

h, a, b = [int(input()) for _ in range(3)]

print((h - a - 1) // (a - b) + 2)