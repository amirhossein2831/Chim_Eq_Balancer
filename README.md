# Chemical Equation Balancer

## Introduction

The Chemical Equation Balancer is a Python package designed to balance chemical equations and perform matrix operations
related to them. This package simplifies the process of balancing complex chemical equations and provides functionality
to work with matrices involved in the process.

## Installation

You can install the Chemical Equation Balancer via pip:

```
pip install chemical_eq_balancer
```

## Usage

### Balancing Chemical Equations

To balance a chemical equation, initialize the balancer with the list of elements and the equation. Then,
call `print_answer()` to get the balanced equation.

```python
from chem_balancer import ChemicalEquationBalancer

elements = ['H', 'O']
equation = 'H2 + O2 -> H2O'

balancer = ChemicalEquationBalancer(elements, equation)
balancer.print_answer()

```

## Accessing Matrix and Equation Information

### Accessing Original Matrix

You can access the original matrix used for balancing with `balancer.original_matrix`.

```python
original_matrix = balancer.original_matrix
```

### Accessing Reduced Echelon Matrix

You can access the reduced echelon matrix obtained during balancing with `balancer.matrix`.

```python
reduced_echelon_matrix = balancer.matrix
```

### Accessing Formula and Elements

You can access the formula and elements used in the equation with `balancer.formula` and `balancer.elements`
respectively.

```python
formula = balancer.formula
elements = balancer.elements
```

## Matrix Operations

### Creating an Echelon Matrix

To create an echelon matrix, use `echelon_maker(matrix)` which give you power to make a matrix in echelon form.
<br>
You can also create reduce echelon matrix, use `reduce_echelon_maker(matrix)`.

```python
import numpy as np
from chem_balancer import ChemicalEquationBalancer

matrix = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0]
])

ce = ChemicalEquationBalancer()
ce.echelon_maker(matrix)
ce.reduce_echelon_maker(matrix)
ce.print_matrix(matrix)
```

### Printing Matrix

You can also print a matrix in a formatted way using `print_matrix(matrix)`.

```python
import numpy as np
from chem_balancer import ChemicalEquationBalancer

matrix = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0]
])

ChemicalEquationBalancer.print_matrix(matrix)
```

# Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue
or submit a pull request on the GitHub repository.

# License

This project is licensed under the MIT License - see the LICENSE file for details.
