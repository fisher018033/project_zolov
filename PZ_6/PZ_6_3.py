#Дан список размера N. Возвести в квадрат все его локальные минимумы (то есть числа, меньшие своих соседей).

try:
  numbers = []
  amount = int(input("Enter amount of numbers: "))
  if amount < 3:
    print('cant')
  else:
    for i in range(amount):
      num = int(input(f"Enter {i+1} number: "))
      numbers.append(num)
    min = []
    def mix(numbers):
      for u in range(1, len(numbers)-1):
        if numbers[u-1] < numbers[u] < numbers[u+1]:
          min.append(numbers[u])
      return min
    print(mix(numbers))
    sq = []
    def mox(min):
      for o in range(len(mix(numbers))):
        o ** 2
        sq.append(min[o])
    print(sq)
    print(mox(min))
except ValueError:
  print('nah')