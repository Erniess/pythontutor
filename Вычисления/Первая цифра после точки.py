# Задача «Первая цифра после точки»
# Условие
# Дано положительное действительное число X. Выведите его первую цифру после
# десятичной точки.

x = float(input())
print(int(x * 10) % 10)