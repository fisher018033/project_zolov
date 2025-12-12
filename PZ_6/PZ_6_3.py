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