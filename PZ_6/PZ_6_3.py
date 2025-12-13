#Дан список размера N. Возвести в квадрат все его локальные минимумы (то есть числа, меньшие своих соседей).

import random
try:
  N = int(input("Введите размер списка: "))
  numbers = [random.randint(1, 100) for _ in range(N)]
  print(f"Случайный список: {numbers}")
  def mix(lst):
    result = lst.copy()
    for i in range(1, len(lst) - 1):
      if lst[i] < lst[i-1] and lst[i] < lst[i+1]:
        result[i] = lst[i] ** 2
    return result
  print(f"Изначальный список: {numbers}")
  print(f"Возведенные в квадрат локальные минимумы: {mix(numbers)}")
except ValueError:
  print('nah')