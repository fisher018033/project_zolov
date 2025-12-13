#Дан список размера N. Найти минимальный из его локальных максимумов (локальный минимум — это элемент, который меньше любого из своих соседей).

import random

try:

  N = int(input("Введите размер списка: "))
  numbers = [random.randint(1, 100) for _ in range(N)]
  print(f"Случайный список: {numbers}")
  local_maxs = []
  if N > 1 and numbers[0] > numbers[1]:
    local_maxs.append(numbers[0])
  elif N == 1:
    local_maxs.append(numbers[0])
  for i in range(1, N - 1):
    if numbers[i - 1] < numbers[i] > numbers[i + 1]:
      local_maxs.append(numbers[i])
  if N > 1 and numbers[-1] > numbers[-2]:
    local_maxs.append(numbers[-1])
  print(f"Локальные максимумы: {local_maxs}")
  if local_maxs:
    min_local_max = min(local_maxs)
    print(f"Минимальный из локальных максимумов: {min_local_max}")
  else:
    print("Локальные максимумы не найдены")

except ValueError:
  print('Ошибка ввода. Введите целое число.')