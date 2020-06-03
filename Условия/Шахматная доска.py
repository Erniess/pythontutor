# Задача «Шахматная доска»
# Условие
# Заданы две клетки шахматной доски. Если они покрашены в один цвет, то выведите слово
# YES, а если в разные цвета — то NO. Программа получает на вход четыре числа от 1 до 8
# каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для
# второй клетки.

x1, x2, y1, y2 = [int(input()) for _ in range(4)]
print('YES' if (x1 + x2) % 2 == (y1 + y2) % 2 else 'NO')

