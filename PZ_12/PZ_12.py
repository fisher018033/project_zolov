# 1. В матрице элементы строки N (N задать с клавиатуры) увеличить на 3.
# 2. В матрице элементы последнего столбца заменить на -1.

import random

rows = 5
cols = 6
matrix = [[random.randint(-10, 20) for _ in range(cols)] for _ in range(rows)]

print("Исходная матрица:")
for row in matrix:
    print(row)

n = int(input("Введите номер строки (0-" + str(rows-1) + "): "))

# Задача 1: элементы строки N увеличить на 3
if 0 <= n < rows:
    matrix[n] = [x + 3 for x in matrix[n]]

# Задача 2: элементы последнего столбца заменить на -1
for i in range(rows):
    matrix[i][-1] = -1

print("\nРезультирующая матрица:")
for row in matrix:
    print(row)