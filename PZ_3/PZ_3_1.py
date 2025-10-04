try:
    A = int(input('Enter first number: '))
    B = int(input('Enter second number: '))
    C = int(input('Enter third number: '))
    if A < B < C or A > B > C: # проверка, стоит ли число B между чилами A и C
        print(True)
    else:
        print(False)
except ValueError:
    print('number...')