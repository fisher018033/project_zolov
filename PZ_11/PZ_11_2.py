#Составить генератор (yield), который преобразует все буквенные символы в строчные.

text = input('Введите строку: ')

def lowercase_generator(iterable):
    for chunk in iterable:
        for char in chunk:
            yield char.lower()

result = ''.join(lowercase_generator(text))
print(result)