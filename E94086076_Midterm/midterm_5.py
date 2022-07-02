import numpy as np


'''
P = (m/2) * (dv/dt) * v
=> dt = (m * v/P) * dv
integral both side to get delta_t
'''

# define Power
P = np.array([4700, 12200, 19000, 31800, 40100, 43800, 43200])
# difine mass
m = 2000
# define velocity
v = np.array([1.0, 1.8, 2.4, 3.5, 4.4, 5.1, 6.0])
# define step size
h = np.zeros(len(v))
for i in range(len(v) - 1):
    h[i] = v[i + 1] - v[i]


# define function
def f(v, P):
    return v / P


# integration
def my_trapezodial(f, h):
    sum = 0
    for i in range(len(f) - 1):
        sum += (f[i] + f[i + 1]) * h[i]
    return sum


f = f(v, P)
delta_t = m * (my_trapezodial(f, h) / 2)
print('t=', delta_t)
