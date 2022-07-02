import numpy as np
from lib.downhill import *
from lib.std import *
from lib.inverse_power import *


def F(x):
    global eVal
    lam = 1000000.0
    min_eVal = 0.4 # limit
    A = np.array([[4*(x[0]**4 + x[1]**4), 2*x[1]**4],
                  [2*x[1]**4, 4*x[1]**4]])
    B = np.array([[4*(x[0]**2 + x[1]**2), -3*x[1]**2],
                 [-3*x[1]**2, 4*x[1]**2]])
                 # change to standard form and do inverse power method
    H, t = stdForm(A, B)
    eVal, eVec = inversePower(H, 0.0)
    return x[0]**2 + x[1]**2 + lam * (max(0, min_eVal - eVal))**2


dStart = np.array([1.0, 1.0])
d = downhill(F, dStart, 0.1)
print("d = ", d)
print("eigenvalue = ", eVal)
