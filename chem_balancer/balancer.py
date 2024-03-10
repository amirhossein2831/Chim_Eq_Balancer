import numpy as np


class ChemicalEquationBalancer:
    def __init__(self, elements: list, formula: str):
        self.elements = elements
        self.formula = formula
        self.matrix = np.ndarray([])

    def parse_equation(self) -> (str, str):
        row_num = len(self.elements)
        l_formula = self.formula.split('->')[0].strip()
        r_formula = self.formula.split('->')[1].strip()
        col_num = len(self.formula.split('+')) + len(self.formula.split('->')) - 1
        self.matrix = np.zeros((row_num, col_num + 1))
        return l_formula, r_formula

    def fill_matrix(self) -> None:
        l_formula, r_formula = self.parse_equation()
        col = 0
        for i in l_formula.split('+'):
            for j in i.split():
                index = self.elements.index(j[0])
                if len(j) == 1:
                    self.matrix[index][col] = 1
                else:
                    self.matrix[index][col] = int(j[1])

            col += 1

        for i in r_formula.split('+'):
            for j in i.split():
                index = self.elements.index(j[0])
                if len(j) == 1:
                    self.matrix[index][col] = -1
                else:
                    self.matrix[index][col] = int(j[1]) * -1

            col += 1

    def echelon_maker(self, matrix: np.ndarray) -> None:
        r, c = matrix.shape
        if r == 0 or c == 0:
            return

        if matrix[0, 0] == 0:
            for j in range(1, r):
                if matrix[j, 0] != 0:
                    matrix[[0, j]] = matrix[[j, 0]]  # Corrected index for swapping
                    break

        for j in range(1, r):
            if matrix[j, 0] != 0:
                multiplier = -matrix[j, 0] / matrix[0, 0]

                matrix[j] += multiplier * matrix[0]

        return self.echelon_maker(matrix[1:, 1:])

    def reduce_echelon_maker(self) -> None:
        r, c = self.matrix.shape
        for i in range(r):
            pivot_col = -1
            for j in range(c):
                if self.matrix[i, j] != 0:
                    pivot_col = j
                    break

            if pivot_col != -1:
                self.matrix[i] /= self.matrix[i, pivot_col]

                for k in range(i):
                    self.matrix[k] -= self.matrix[k, pivot_col] * self.matrix[i]
