# Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Среднее арифметическое элементов:
# Положительные четные элементы:
# Сумма положительных четных элементов:
# Среднее арифметическое положительных четных элементов:

numbers = [12, -5, 8, -3, 24, 7, -10, 16, -8, 5, 18, -2]

with open('data7.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join(map(str, numbers)))

print("Файл data7.txt успешно создан.")

with open('data7.txt', 'r', encoding='utf-8') as f:
    data = f.read().strip().split()
    nums = [int(x) for x in data]

total_count = len(nums)
total_sum = sum(nums)
average = total_sum / total_count if total_count > 0 else 0

positive_even = [x for x in nums if x > 0 and x % 2 == 0]
sum_positive_even = sum(positive_even)
avg_positive_even = sum_positive_even / len(positive_even) if positive_even else 0

with open('result7.txt', 'w', encoding='utf-8') as f:
    f.write("Исходные данные:\n")
    f.write(' '.join(map(str, nums)) + '\n\n')
    f.write(f"Количество элементов: {total_count}\n")
    f.write(f"Среднее арифметическое элементов: {average:.2f}\n")
    f.write(f"Положительные четные элементы: {positive_even}\n")
    f.write(f"Сумма положительных четных элементов: {sum_positive_even}\n")
    f.write(f"Среднее арифметическое положительных четных элементов: {avg_positive_even:.2f}\n")

print("Файл result7.txt успешно создан.")