# Задача «Больше своих соседей»
# Условие
# Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух
# своих соседей, и выведите количество таких элементов. Крайние элементы списка никогда
# не учитываются, поскольку у них недостаточно соседей.

li = [int(i) for i in input().split()]
count = 0
for i in range(1, len(li) - 1):
    if li[i - 1] < li[i] and li[i + 1] < li[i]:
        count += 1
print(count)
