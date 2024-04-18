# 2) Найти самое длинное слово из массива. Реализовать двумя видами циклов

mass = ['УГАТУ', 'Hello', 'word', 'Интеллектуальный', 'код']

word1 = ''
for i in mass:
    if len(i) > len(word1):
        word1 = i
print(f'Способ №1: {word1}')

word2 = ''
j = 0
while j < len(mass):
    if len(mass[j]) > len(word2):
        word2 = mass[j]
    j += 1
print(f'Способ №2: {word2}')

