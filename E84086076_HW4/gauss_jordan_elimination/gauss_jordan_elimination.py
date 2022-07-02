import numpy as np
from gauss_jordan_function import *


# test values
a = np.array([[1, 2, 3], [3, 4, 5], [3, 5, 5]])
y = np.array([2, 2, 5])
a1 = np.array([[1, 2, 3, 4], [5, 4, 3, 2], [2, 1, 2, 4], [2, 1, 3, 4]])
y1 = np.array([4, 8, 5, 6])
# place matrices into the list in order not to repeat the output code later
list = [a, a1, y, y1]


# calculate answer
for index in range(2):
    # print title
    print("Sample", index + 1)
    # initilize gauss_matrix
    gauss_matrix = gauss_init(list[index], list[index + 2])
    print("diagonal matrix:")
    # do elimination
    gauss_matrix_eliminated = elimination(gauss_matrix)
    print(gauss_matrix_eliminated)
    print("x:")
    # solve gauss_matrix_eliminated
    answer = solve(gauss_matrix_eliminated)
    print(answer)
