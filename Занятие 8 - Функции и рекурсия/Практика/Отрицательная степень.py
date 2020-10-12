# Задача «Отрицательная степень»
# Условие
#
# Дано действительное положительное число a и целоe число n.
#
# Вычислите an. Решение оформите в виде функции power(a, n).
#
# Стандартной функцией возведения в степень пользоваться нельзя.

def power(a, n):
    ans = 1
    for _ in range(abs(n)):
        ans *= a
    if n >= 0: return ans
    else: return 1 / ans

a, n = float(input()), int(input())

print(power(a, n))