# Создайте класс «Матрица», который имеет атрибуты количества строк и столбцов. Добавьте методы для сложения, вычитания и умножения матриц.

class Matrix:
    def __init__(self, rows, cols, data=None):
        self.rows = rows
        self.cols = cols
        if data is None:
            self.data = [[0 for _ in range(cols)] for _ in range(rows)]
        else:
            self.data = data

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы разных размеров")
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] 
                  for i in range(self.rows)]
        return Matrix(self.rows, self.cols, result)

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы разных размеров")
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] 
                  for i in range(self.rows)]
        return Matrix(self.rows, self.cols, result)

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Несовместимые размеры для умножения")
        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) 
                   for j in range(other.cols)] for i in range(self.rows)]
        return Matrix(self.rows, other.cols, result)


# Тестовые запуски
print("=== Тест класса Matrix ===")
m1 = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
m2 = Matrix(2, 3, [[7, 8, 9], [10, 11, 12]])

print("Матрица 1:")
print(m1)
print("\nМатрица 2:")
print(m2)

print("\nСложение:")
print(m1.add(m2))

print("\nВычитание:")
print(m1.subtract(m2))

m3 = Matrix(3, 2, [[1, 2], [3, 4], [5, 6]])
print("\nУмножение:")
print(m1.multiply(m3))