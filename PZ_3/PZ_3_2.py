KG = 1 # 1 кг
MG = 1000000 # 1 000 000 мг в одном кг
G = 1000 # 1000 грамм в одном кг
T = 1000 # 1000 кг в одной тонне
CE = 100 # 100 кг в одном центнере
number = int(input('Enter a number from 1 to 5: '))
if number > 5 or number < 1:
    print('I SAID FROM 1 TO 5')
size = int(input('Enter size: '))
if number == 1:
    print(size)
if number == 2:
    print(size/MG)
if number == 3:
    print(size/G)
if number == 4:
    print(size * T)
if number == 5:
    print(size * CE)