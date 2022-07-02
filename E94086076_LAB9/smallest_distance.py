from powell import *
from numpy import array


def F(x):
    lam = 1.0
    c = x[0] * x[1] - 5.0
    return distSq(x) + lam * c**2


# distance function
def distSq(x):
    return (x[0] - 5)**2 + (x[1] - 8)**2


xStart = array([1.0, 5.0])
xMin, nIter = powell(F, xStart, 0.01)
print("Intersection point =", xMin)
print("Minimum distance =", math.sqrt(distSq(xMin)))
print('xy =', xMin[0] * xMin[1])
print("Number of cycles =", nIter)
