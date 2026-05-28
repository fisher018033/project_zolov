with open('text18-7.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()

lower_count = sum(1 for line in text for char in line if char.islower() and char.isalpha())

print("Содержимое файла text18-7.txt:")
print(''.join(text), end='')
print(f"\nКоличество букв в нижнем регистре: {lower_count}")

if len(text) >= 3:
    last_line = text.pop()
    text.insert(2, last_line)

with open('text18-7_modified.txt', 'w', encoding='utf-8') as f:
    f.writelines(text)