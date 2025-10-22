#Описать функцию AddRightDigit(D, K), добавляющую к целому положительному числу K справа цифру D (D — входной параметр целого типа, лежащий в диапазоне 0-9, K — параметр целого типа, являющийся одновременно входным и выходным). С помощью этой функции последовательно добавить к данному числу K справа данные цифры D1 и D2, выводя результат каждого добавления.

try:
  bas = int(input('введите число: '))
  ad = int(input('введите число от 0 до 9 для добавления к базовому: '))
  ad2 = int(input('введите второе число от 0 до 9 для добавления к предыдущему: '))
  if ad < 0 or ad > 9 or ad2 < 0 or ad2 > 9:
    print('ОТ 0 ДО 9')
  else:
    def AddRightDigit(bas, ad):
      return str(bas) + str(ad)
    bas = AddRightDigit(bas, ad)
    def AddAgain(bas, ad2):
      return str(bas) + str(ad2)
    bas2 = AddAgain(bas, ad2)
    print(bas)
    print(bas2)
except ValueError:
  print('Неверно')