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

   