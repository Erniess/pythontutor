# Задача «Замена внутри фрагмента»
# Условие
#
# Дана строка. Замените в этой строке все появления буквы h на букву H,
# кроме первого и последнего вхождения.

word = str(input())

a = word[:word.find('h') + 1]
b = word[word.find('h') + 1:word.rfind('h')].replace('h', 'H')
c = word[word.rfind('h'):]
word.replace('h', 'H', 1)

print(a + b + c)