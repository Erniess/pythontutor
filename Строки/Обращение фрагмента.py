# Задача «Обращение фрагмента»
# Условие
#
# Дана строка, в которой буква h встречается как минимум два раза. Разверните
# последовательность символов, заключенную между первым и последним появлением
# буквы h, в противоположном порядке.

word = str(input())

print(word[:word.find('h') + 1] +
      word[word.find('h') + 1 : word.rfind('h')][::-1] +
      word[word.rfind('h'):])