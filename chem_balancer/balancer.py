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


