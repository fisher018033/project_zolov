#Дан список размера N. Найти минимальный из его локальных максимумов (локальный минимум — это элемент, который меньше любого из своих соседей).

try:
  numbers = []
  amount = int(input("Enter amount of numbers: "))
  if amount < 3:
    print('cant')
    for i in range(amount):
      num = int(input(f"Enter {i+1} number: "))
      numbers.append(num)
except ValueError:
  print('nah')