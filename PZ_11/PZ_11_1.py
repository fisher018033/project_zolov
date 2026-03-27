# Организовать и вывести последовательность из N случайных целых чисел. Из исходной последовательности организовать первую последовательность, содержащую четные числа, и вторую – для всех остальных. Найти среднее арифметическое в полученных последовательностях.

import random

try:
  fir = int(input('enter a number to start: '))
  sec = int(input('enter a number to finish: '))
  num = []
  for col in range(num):
    n = random.randint(fir, sec)
    num.append(n)
  print(num)

except ValueError:
  print('Error')
