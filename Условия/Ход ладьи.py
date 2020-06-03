# Задача «Ход ладьи»
# Условие
# Шахматная ладья ходит по горизонтали или вертикали. Даны две различные клетки
# шахматной доски, определите, может ли ладья попасть с первой клетки на вторую
# одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие
# номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
# Программа должна вывести YES, если из первой клетки ходом ладьи можно попасть во
# вторую или NO в противном случае.

x1, y1, x2, y2 = [int(input()) for _ in range(4)]
print('YES' if x1 == x2 or y1 == y2 else 'NO')