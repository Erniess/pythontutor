# Задача «Минимум из трех чисел»
# Условие
# Даны три целых числа. Выведите значение наименьшего из них.

a, b, c = [int(input()) for _ in range(3)]
print(a if a <= b and a <= c else b if b <= c else c)
