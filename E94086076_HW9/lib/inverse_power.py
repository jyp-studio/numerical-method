# module inversePower
''' lam,x = inversePower(a,s,tol=1.0e-6).
Inverse power method for solving the eigenvalue problem
[a]{x} = lam{x}. Returns ’lam’ closest to ’s’ and the
corresponding eigenvector {x}.
'''
import numpy as np
from lib.LU import *
import math
from random import random


def inversePower(a, s, tol=1.0e-6):
    n = len(a)
    aStar = a - np.identity(n)*s  # Form [a*] = [a] - s[I]
    aStar = LUdecomp(aStar)  # Decompose [a*]
    x = np.zeros(n)
    for i in range(n):  # Seed [x] with random numbers
        x[i] = random()
    xMag = math.sqrt(np.dot(x, x))  # Normalize [x]
    x = x/xMag
    for i in range(50):  # Begin iterations
        xOld = x.copy()  # Save current [x]
        x = LUsolve(aStar, x)  # Solve [a*][x] = [xOld]
        xMag = math.sqrt(np.dot(x, x))  # Normalize [x]
        x = x/xMag
        if np.dot(xOld, x) < 0.0:  # Detect change in sign of [x]
            sign = -1.0
            x = -x
        else:
            sign = 1.0
        if math.sqrt(np.dot(xOld - x, xOld - x)) < tol:
            return s + sign/xMag, x
    print('Inverse power method did not converge')
