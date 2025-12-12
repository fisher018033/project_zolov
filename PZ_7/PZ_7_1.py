#Дана непустая строка. Вывести коды ее первого и последнего символа

try:
  line = input("Введите строчку: ")
  first = line[0]
  last = line[-1]
  first_code = ord(line[0])
  last_code = ord(line[-1])
  print(f'Первый символ: {first} и его код {first_code}')
  print(f'Первый символ: {last} и его код {last_code}')
except Exception as e:
  print('nah')