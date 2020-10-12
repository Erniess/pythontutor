# Задача «Вставить элемент»
# Условие
# Дан список целых чисел, число k и значение C. Необходимо вставить в список на
# позицию с индексом k элемент, равный C, сдвинув все элементы, имевшие индекс не
# менее k, вправо.
#
# Поскольку при этом количество элементов в списке увеличивается, после считывания
# списка в его конец нужно будет добавить новый элемент, используя метод append.
#
# Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе
# и не создавая дополнительного списка.

li = [int(i) for i in input().split()]
k, c = map(int, input().split())
li.append('')
for i in range(len(li) - 1, k, -1):
    li[i] = li[i - 1]
li[k] = c
print(' '.join(map(str, li)))