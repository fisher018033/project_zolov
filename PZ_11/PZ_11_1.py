# Организовать и вывести последовательность из N случайных целых чисел. Из исходной последовательности организовать первую последовательность, содержащую четные числа, и вторую – для всех остальных. Найти среднее арифметическое в полученных последовательностях.

import random

try:
  ent = int(input('Сколько хотите чисел в списке?:'))
  num = []
  ch_num = []
  oth_num = []

  for col in range(ent):
    n = random.randint(1,100)
    num.append(n)

  for ch in num:
    if ch % 2 == 0:
      ch_num.append(ch)
    else:
      oth_num.append(ch)

  print(f'Исходная последовательность: {num}')
  print(f'Четные числа: {ch_num}')
  print(f'Остальные числа: {oth_num}')
  print(f'Среднее арифметическое четных чисел: {sum(ch_num)/len(ch_num)}')
  print(f'Среднее арифметическое остальных чисел: {sum(oth_num)/len(oth_num)}')
except ValueError:
  print('Error')