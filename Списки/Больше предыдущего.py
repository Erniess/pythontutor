# Задача «Больше предыдущего»
# Условие
# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

li = input().split()
print(' '.join([li[i] for i in range(1, len(li)) if li[i] > li[i - 1]]))