# Задача «Факториал»
# Условие
# Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
#
# По данному натуральному n вычислите значение n!. Пользоваться математической
# библиотекой math в этой задаче запрещено.

f = 1
for i in range(f, int(input()) + 1):
    f *= i
print(f)