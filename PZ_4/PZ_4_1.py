#Даны два целых числа A и B (A < Б). Найти произведение всех целых чисел от A до B включительно.

try:
  A = int(input('Введи первое значение: '))
  B = int(input('Введи второе значение: '))
  if A >= B:
    print('A должно быть меньше B')
  else:
    k = 1
    for mult in range(A, B + 1):
      k *= mult
    print(k)
except ValueError:
  print('Неверно')
