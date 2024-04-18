# 6) Подсчитать количество цифр в числе. Реализовать двумя видами циклов

n = int(input('Введите число: '))

count1 = 0
num1 = n
while num1 > 0:
    num1 //= 10
    count1 += 1

count2 = 0
for i in range(1, len(str(n)) + 1):
    count2 += 1
    
print(f'Способ №1 = {count1}')
print(f'Способ №2 = {count2}')
