# 11) Напечатать календарь месяца, предполагая, что месяц начинается в понедельник и имеет 31 день

day = ""
i = 0

while i < 32:
    if i == 0:
        print("Пн Вт Ср Чт Пт Сб Вс")
        i += 1
        continue
    i_str = str(i)
    if len(i_str) == 1:
        i_str = f" {i_str}"
    day += i_str + " "
    if i % 7 == 0 and i < 31:
        print(day)
        day = ""
    i += 1

print(day)