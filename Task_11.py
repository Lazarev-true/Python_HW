# Создайте класс Матрица. Добавьте методы для: вывода на печать, 
# проверку на равенство, сложения, *умножения матриц


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def eq(self, other):
        return self.matrix == other.matrix

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            return 'Матрицы имеют разный размер, их нельзя сложить'
        else:
            result = []
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(self.matrix[0])):
                    row.append(self.matrix[i][j] + other.matrix[i][j])
                result.append(row)
            return Matrix(result)

    def __mul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            return 'Матрицы нельзя перемножить'
        else:
            result = []
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(other.matrix[0])):
                    s = 0
                    for k in range(len(other.matrix)):
                        s += self.matrix[i][k] * other.matrix[k][j]
                    row.append(s)
                result.append(row)
            return Matrix(result)
        

matrix_1 = Matrix([[1, 2], [3, 4]])
matrix_2 = Matrix([[1, 2, 3],[4, 5, 6]])
print(matrix_1)
print()
print(matrix_2)
print()
print(matrix_1 == matrix_2)
print()
print(matrix_1 + matrix_2)
print()
print(matrix_1 * matrix_2)
