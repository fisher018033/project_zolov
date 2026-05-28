import random

n = 12
a = [random.randint(-20, 20) for _ in range(n)]

even = [x for x in a if x % 2 == 0]
odd = [x for x in a if x % 2 != 0]

avg_even = sum(even) / len(even) if even else 0
avg_odd = sum(odd) / len(odd) if odd else 0

print("Исходная последовательность:", a)
print("Четные числа:", even)
print("Нечетные числа:", odd)
print("Среднее арифметическое четных:", round(avg_even, 2))
print("Среднее арифметическое нечетных:", round(avg_odd, 2))