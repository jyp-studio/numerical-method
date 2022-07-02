import numpy as np


def gauss_init(A, y):
    '''combine A and y to a single matrix'''
    # first reshape y
    y = np.reshape(y, (len(y), 1))
    # second concat a and y and change type to float
    gauss_matrix = np.hstack((A, y)).astype(float)
    return gauss_matrix


def elimination(gauss_matrix):
    '''eliminate matrix to unit diagonal form'''
    # get dimension of gauss_matrix
    gauss_row, gauss_column = gauss_matrix.shape
    # make all lower-triangle row bocomes 0 and switch to right-second column
    # gauss_column - 2: gauss_column - y - last column
    for column in range(gauss_column - 2):
        for row in range(column + 1, gauss_row):  # row = column + 1
            # calculate times
            times = -(gauss_matrix[row][column] / gauss_matrix[column][column])

            # do elimination
            gauss_matrix[row] = gauss_matrix[column] * \
                times + gauss_matrix[row]

    # make all upper-triangle row bocomes 0 and switch to left-second column
    for column in range(gauss_column - 2, 0, -1):  # gauss_column - y - first column
        for row in range(column - 1, -1, -1):  # row = column - 1
            # calculate times
            times = -(gauss_matrix[row][column] / gauss_matrix[column][column])

            # do elimination
            gauss_matrix[row] = gauss_matrix[column] * \
                times + gauss_matrix[row]

    # reduce to unit
    for row in range(gauss_row):
        gauss_matrix[row] = gauss_matrix[row] / gauss_matrix[row][row]
    return gauss_matrix


def solve(gauss_matrix):
    '''solve Ax = y'''
    # create an answer list
    answer = []
    # get dimension of gauss_matrix
    gauss_row, gauss_column = gauss_matrix.shape
    # append answer to answer list
    for i in range(gauss_row):
        answer.append(gauss_matrix[i][gauss_column - 1] / gauss_matrix[i][i])
    return answer
