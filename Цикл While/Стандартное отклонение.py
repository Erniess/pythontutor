# Задача «Стандартное отклонение»
# Условие
#
# Дана последовательность натуральных чисел x1
# , x2, ..., xn. Стандартным отклонением называется величина
# σ=(x1−s)2+(x2−s)2+…+(xn−s)2n−1‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾√
# где s=x1+x2+…+xnn
#
#  — среднее арифметическое последовательности.
#
# Определите стандартное отклонение для данной последовательности натуральных чисел,
# завершающейся числом 0.

nat_range = []
n_summ = 0
n = int(input())
while n != 0:
    nat_range.append(n)
    n_summ += n
    n = int(input())
n = len(nat_range)
s = sum(nat_range) / n
betta = (sum([(i - s) ** 2 for i in nat_range]) / (n - 1)) ** 0.5
print(betta)
