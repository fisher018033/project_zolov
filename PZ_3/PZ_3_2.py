#Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер. Дан номер единицы массы (целое число в диапазоне 1-5) и масса тела в этих единицах (вещественное число). Найти массу тела в килограммах

KG = 1 # 1 кг
MG = 1000000 # 1 000 000 мг в одном кг
G = 1000 # 1000 грамм в одном кг
T = 1000 # 1000 кг в одной тонне
CE = 100 # 100 кг в одном центнере
try:
    number = int(input('Enter a number from 1 to 5: ')) #Выбор единицы массы
    if number > 5 or number < 1:
        print('I SAID FROM 1 TO 5')
    size = int(input('Enter size: ')) #Масса тела в этой единице
    if size < 0:
        print('ANTIMATTER') #Масса не может быть отрицательна, либо это антиматерия
    elif number == 1:
        print(size)
    elif number == 2:
        print(size/MG)
    elif number == 3:
        print(size/G)
    elif number == 4:
        print(size * T)
    elif number == 5:
        print(size * CE)
except ValueError:
    print('need number >:(')
