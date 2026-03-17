import numpy as np


class Matrix:
    eps = 1e-12

    def __init__(self, n):
        self.n = n
        self.matrix = []
        self.triangle_matrix = []
        self.det = 0
        self.answer = [0] * n
        self.residual = [0] * n

    def append(self, row):
        self.matrix.append(row)

    def set_matrix(self, matrix):
        self.matrix = self.copy_matrix(matrix)

    def find_answer(self):
        triangle_matrix = self.copy_matrix(self.triangle_matrix)
        if abs(self.det) < self.eps: return
        for i in range(self.n - 1, -1, -1):
            self.answer[i] = triangle_matrix[i][-1] / triangle_matrix[i][i]
            for j in range(i):
                triangle_matrix[j][-1] -= triangle_matrix[j][i] * self.answer[i]
                triangle_matrix[j][i] = 0

    def find_residual(self):
        if abs(self.det) < self.eps: return
        for i in range(self.n):
            self.residual[i] = self.matrix[i][-1]
            for j in range(self.n):
                self.residual[i] -= self.matrix[i][j] * self.answer[j]

    def calculate(self):
        n = self.n
        matrix = self.copy_matrix(self.matrix)
        count = 0
        for i in range(n):
            l = i
            for m in range(i + 1, n):
                if abs(matrix[m][i]) > abs(matrix[l][i]):
                    l = m
            if l != i:
                count += 1
                matrix[i], matrix[l] = matrix[l], matrix[i]
            for j in range(i + 1, n):
                if abs(matrix[i][i]) < self.eps:
                    self.det = 0
                    return
                cf = -matrix[j][i] / matrix[i][i]
                matrix[j] = [matrix[j][k] + cf * matrix[i][k] for k in range(len(matrix[i]))]
        self.triangle_matrix = matrix
        self.det = (-1) ** count
        for i in range(n):
            self.det *= self.triangle_matrix[i][i]
        self.find_answer()
        self.find_residual()

    def copy_matrix(self, matrix):
        return [row[:] for row in matrix]

    def compare(self):
        if abs(self.det) < self.eps:
            return "Матрица является вырожденной, сравнение результатов невозможно"
        A = np.array([row[:-1] for row in self.matrix], dtype=float)
        b = np.array([row[-1] for row in self.matrix], dtype=float)
        answer_numpy = np.linalg.solve(A, b)
        det_numpy = np.linalg.det(A)
        residual_numpy = b - A @ answer_numpy

        return (f"""Под пунктом 1 записывается результат, полученный с помощью Метода Гаусса
Под пунктом 2 записывается результат, полученный использованием готовой библиотеки NumPy

Определители:
1.{self.det}
2.{det_numpy}

Векторы неизвестных:
1.{self.answer}
2.{answer_numpy.tolist()}

Векторы невязок:
1.{self.residual}
2.{residual_numpy.tolist()}
""")
