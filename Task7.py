# 7) Проверить, является ли строка палиндромом (зеркальная)

s = input('Введите строку: ')
s = s.lower()
start = 0
end = len(s) - 1
is_polid = True

for i in range(len(s) // 2):
    if s[start] != s[end]:
        is_polid = False
        break
    start += 1
    end -= 1

if is_polid:
    print(f"Слово '{s}' является палиндромом")
else:
    print(f"Слово '{s}' не является палиндромом")
