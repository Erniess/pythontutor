# Задача «Количество различных элементов»
# Условие
# Дан список, упорядоченный по неубыванию элементов в нем.
# Определите, сколько в нем различных элементов.
# li = set(int(i) for i in input().split())
# print(len(li))

li = [int(i) for i in input().split()]
count = 1
for i in range(len(li) - 1):
    if li[i] < li[i + 1]:
        count += 1
print(count)