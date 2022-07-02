import numpy as np
from gauss_jordan_elimination.gauss_jordan_function import gauss_init, elimination, solve


# test values
a = np.array([[1, 2, 3], [3, 4, 5], [3, 5, 5]])
y = np.array([2, 2, 5])
a1 = np.array([[1, 2, 3, 4], [5, 4, 3, 2], [2, 1, 2, 4], [2, 1, 3, 4]])
y1 = np.array([4, 8, 5, 6])
list = [a, a1, y, y1]


def get_LU(matrix):
    '''do LU decomposition'''
    # initialization
    U_matrix = np.copy(matrix)  # initial U_matrix as a copy of original matrix
    rows, columns = U_matrix.shape  # get dimension of U_matrix
    L_matrix = np.eye(rows, dtype=float)  # initial L as a identity matrix

    # make all lower-triangle row bocomes 0 and switch to right-second column
    for column in range(columns - 1):  # column - 1: gauss_column - last column
        for row in range(column + 1, rows):  # row = column + 1
            # calculate times
            times = -(U_matrix[row][column] / U_matrix[column][column])

            # fill L_matrix
            L_matrix[row][column] = - times

            # do elimination
            U_matrix[row] = U_matrix[column] * times + U_matrix[row]

    return L_matrix, U_matrix


# calculate answer
for index in range(2):
    # print title
    print("Sample", index + 1)
    L_matrix, U_matrix = get_LU(list[index])
    print("u_matrix:")
    print(U_matrix)
    print("l_matrix:")
    print(L_matrix)
    print("x:")
    M_matrix = gauss_init(list[index], list[index + 2])
    x = solve(elimination(M_matrix))
    print(x)
