# 8) Определить, содержит ли список дубликаты

lst = [1, 2, 3, 4, 5, 1, 8]
is_dublikat = False

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j]:
            is_dublikat = True

if is_dublikat:
    print(f"Список {lst} содержит дубликаты")
else:
    print(f"Список {lst} не содержит дубликаты")