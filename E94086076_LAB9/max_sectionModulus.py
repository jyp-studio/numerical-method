from goldSearch import *

# parameter
B = 48.0
H = 60.0


def f(y):
    a = B * (H - y) / H
    b = (B - a) / 2.0
    A = (B + a) * y / 2.0
    Q = (a * y**2) / 2.0 + 2.0 * (b*y/2) * y / 3.0
    d = Q / A
    c = y - d
    I = (a * y**3) / 3.0 + 2.0 * (b * y**3 / 12.0)
    I_bar = I - A * d**2
    return -I_bar / c


yStart = 60.0
h = 1.0
y1, y2 = bracket(f, yStart, h)
y, fMin = search(f, y1, y2)
print("Optimal y =", y)
print("Optimal S =", -fMin)
print('S of triangle =', -f(yStart))
