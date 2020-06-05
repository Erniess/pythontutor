# Задача «Первое и последнее вхождения»
# Условие
#
# Дана строка. Если в этой строке буква f встречается только один раз, выведите её
# индекс. Если она встречается два и более раз, выведите индекс её первого и последнего
# появления. Если буква f в данной строке не встречается, ничего не выводите.
#
# При решении этой задачи не стоит использовать циклы.

word = str(input())
print('' if word.count('f') == 0 else word.find('f'),
      '' if word.count('f') <= 1 else word.rfind('f'))