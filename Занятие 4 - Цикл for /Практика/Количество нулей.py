# Задача «Количество нулей»
# Условие
# Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел.
# Подсчитайте количество нулей среди введенных чисел и выведите это количество.
# Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.

print(sum([1 for i in range(int(input())) if int(input()) == 0]))