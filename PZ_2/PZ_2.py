#Дана масса M в килограммах. Используя операцию деления нацело, найти количество полных тонн в ней (1 тонна = 1000 кг)

try:
    M = int(input('enter size in kg: '))
    T = 1000  # 1000 kg in 1 tonn
    if M < 0:
        print("ANTIMATTER") #Масса не может быть отрицательной, либо это антиматерия
    else:
      print(M // T, 'tonn')
except ValueError:
    print('I SAID SIZE')
