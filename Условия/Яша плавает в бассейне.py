# Задача «Яша плавает в бассейне»
# Условие
# Яша плавал в бассейне размером N × M метров и устал. В этот момент он обнаружил,
# что находится на расстоянии x метров от одного из длинных бортиков (не обязательно
# от ближайшего) и y метров от одного из коротких бортиков. Какое минимальное расстояние
# должен проплыть Яша, чтобы выбраться из бассейна на бортик? Программа получает на вход
# числа N, M, x, y. Программа должна вывести число метров, которое нужно проплыть Яше до
# бортика.

N, M, x, y = [int(input()) for _ in range(4)]
if N <= M:
    N, M = M, N
print(min(x, M - x, y, N - y))