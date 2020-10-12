# Задача «Максимальное число идущих подряд равных элементов»
# Условие
# Дана последовательность натуральных чисел, завершающаяся числом 0. Определите,
# какое наибольшее число подряд идущих элементов этой последовательности равны друг
# другу.

n = int(input())
count = 1
max_count = 1
pattern_val = 0
while n != 0:
    if n == pattern_val:
        count += 1
    else:
        pattern_val = n
        count = 1
    max_count = max(count, max_count)
    n = int(input())
print(max_count)