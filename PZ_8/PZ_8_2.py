# Дана строка 'груши 45 991 63 100 12 морковь 13 47 26 0 16', отражающая продажи продукции по дням в кг. Преобразовать информацию из строки в словари, с использованием функции найти минимальные продажи по каждому виду продукции, результаты вывести на экран.

s = 'груши 45 991 63 100 12 морковь 13 47 26 0 16'
print('Исходная строка:', s)
print()
try:
    d = s.split()
    res = {}
    prod = None
    ch = []
    for i in d:
        if i.isdigit():
            ch.append(int(i))
        else:
            if prod:
                res[prod] = ch
            prod = i
            ch = []
    if prod:
        res[prod] = ch
    print('Результат:')
    for k, v in res.items():
        print(f'{k}: {min(v)} кг')
except ValueError:
    print("Ошибка")
