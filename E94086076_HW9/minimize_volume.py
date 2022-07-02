from lib.powell import *
import numpy as np
from lib.gauss_elimination import my_gauss_elimination

# parameters
E = 1
L = 1
P = 1
delta = 1


def F(x):
    global v, weight
    lam = 100
    coef = 2 * np.sqrt(2) # coeficient
    A = np.array([[coef*x[1] + x[2], -x[2], x[2]],
                  [-x[2], x[2], -x[2]],
                  [x[2], -x[2], coef*x[0] + x[2]]]) / coef
    b = np.array([0, -1, 0])
    # do gauss elimination
    v = my_gauss_elimination(A, b)
    weight = x[0] + x[1] + np.sqrt(2.0)*x[2]
    # define penalty
    penalty = max(0.0, abs(v[1]) - 1.0)**2 + max(0.0, -x[0])**2 \
        + max(0.0, -x[1])**2 + max(0.0, -x[2])**2
    return weight + lam * penalty


xStart = np.array([1.0, 1.0, 1.0])
x, numIter = powell(F, xStart)
print("x = ", x)
print("v = ", np.around(v, decimals=8))
print("Relative weight F = ", np.round(weight, 10))
print("Number of cycles = ", numIter)
