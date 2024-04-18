"""
9) Удалить все дубликаты из списка без использования дополнительных структур.
Реализовать двумя видами циклов, для удаления можно использовать pop() либо del
"""

lst1 = [1, 2, 3, 4, 1, 2, 6, 7, 8]
lst2 = [1, 2, 3, 4, 1, 2, 6, 7, 8]



for e in lst1:
    for k in range(lst1.count(e)-1):
        lst1.remove(e)

i = 0
while i < len(lst2):
    j = i + 1
    while j < len(lst2):
        if lst2[i] == lst2[j]:
            lst2.pop(j)
            j -= 1
        else:
            j += 1
    i += 1

print(f'Через цикл for: {lst1}')
print(f'Через цикл while: {lst2}')