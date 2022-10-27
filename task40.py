"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
величин, расположенных в виде прямоугольной схемы. Примеры матриц вы найдете в методичке. Следующий шаг — реализовать
перегрузку метода str() для вывода матрицы в привычном виде. Далее реализовать перегрузку метода add() для реализации
операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д. """

class Matrix:
    def __init__(self, matrix):
        self.our_matrix = matrix

    def __str__(self):
        for i in range(len(self.our_matrix)):
            print(self.our_matrix[i])
        return "Matrix with " + str(len(self.our_matrix)) + " rows, and " + str(len(self.our_matrix[0])) + " columns."

    def __add__(self, other):
        new_matrix = []
        buffer = []
        if len(self.our_matrix) == len(other.our_matrix) and len(self.our_matrix[0]) == len(other.our_matrix[0]):
            for i in range(len(self.our_matrix)):
                for j in range(len(self.our_matrix[0])):
                    buffer.append(int(self.our_matrix[i][j]) + int(other.our_matrix[i][j]))
                new_matrix.append(buffer)
                buffer = []
            return Matrix(new_matrix)
        else:
            print("Matrix's must be with equal dimensions")
            return 0


matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
new_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matrix)

new_matrix = matrix + new_matrix

print(new_matrix)