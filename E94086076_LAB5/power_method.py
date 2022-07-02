import numpy as np


# test values
x = np.array([1, 1, 1])
a = np.array([[2, 0, 1], [-1, 4, -1], [-1, 2, 0]])
x1 = np.array([1, 1])
a1 = np.array([[2, 4], [3, 6]])
list = [a, a1, x, x1]


def normalize(matrix):
    '''get the matrix's max value then div it'''
    max = abs(matrix).max()
    return matrix / max, max


def power_method(matrix, eignenvector) -> np.array:
    '''find eignevector and eignevalues'''
    last_eigenvalue = None

    while True:
        # get eignenvector
        eignenvector = np.dot(matrix, eignenvector).astype(float)
        # normalize
        eignenvector, eignenvalue = normalize(eignenvector)
        if last_eigenvalue == eignenvalue:
            return eignenvector, last_eigenvalue
        else:
            last_eigenvalue = eignenvalue


# print values
for i in range(2):
    print("Sample", i + 1)
    eignenvector, eignenvalue = power_method(list[i], list[i+2])
    print('Eigenvalue:', eignenvalue)
    print('Eigenvector:', eignenvector)
    print('-----------------------------')
