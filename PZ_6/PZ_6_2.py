#Дан список размера N. Найти минимальный из его локальных максимумов (локальный минимум — это элемент, который меньше любого из своих соседей).

try:
  numbers = []
  amount = int(input("Enter amount of numbers: "))
  if amount < 3:
    print('cant')
  else:
    for i in range(amount):
      num = int(input(f"Enter {i+1} number: "))
      numbers.append(num)
    max = []
    def mix(numbers):
      for u in range(1, len(numbers)-1):
        if numbers[u-1] < numbers[u] > numbers[u+1]:
          max.append(numbers[u])
      return max
    min_max = min(mix(numbers))
    print(min_max)
except ValueError:
  print('nah')