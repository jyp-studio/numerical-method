import numpy as np
from numpy.linalg import inv
from power_method import power_method


# initialize values
x = np.array([1, 1])
a = np.array([[0, 2], [2, 3]])
x1 = np.array([1, 1, 1])
a1 = np.array([[1, 5, 2], [2, 4, 3], [2, 1, 6]])
list = [x, x1, a,  a1]

# test values
for i in range(2):
    print('Sample', i + 1)
    # inverse matrix
    a_inverse = inv(list[i + 2])
    # power method
    eignenvector, eigenvalue = power_method(a_inverse, list[i])
    print('The Minimum Eigenvalue:', 1 / eigenvalue)
    print('Eigenvector:', eignenvector)
    print('------------------------')
