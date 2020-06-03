# Задача «Стоимость покупки»
# Условие
# Пирожок в столовой стоит a рублей и b копеек. Определите, сколько рублей и
# копеек нужно заплатить за n пирожков. Программа получает на вход три числа:
# a, b, n, и должна вывести два числа: стоимость покупки в рублях и копейках.

a, b, n = [int(input()) for _ in range(3)]
costInPenny = n * (100 * a + b)
print(costInPenny // 100, costInPenny % 100)