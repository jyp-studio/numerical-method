from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn-poster")


def my_RK4(ds, t_span, s0):
    # initial S to zeros
    s = np.zeros((len(t_span)))
    # set first of s to the value of s0
    s[0] = s0
    # find step size
    h = (t_span[-1] - t_span[0]) / (len(t_span) - 1)
    # do RK4
    for i in range(len(t_span) - 1):
        k1 = ds(t_span[i], s[i])
        k2 = ds(t_span[i] + (h/2), s[i] + (1/2) * k1 * h)
        k3 = ds(t_span[i] + (h/2), s[i] + (1/2) * k2 * h)
        k4 = ds(t_span[i] + h, s[i] + k3 * h)
        s[i + 1] = s[i] + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
    return t_span, s


def f(t, s):
    return np.sin(np.exp(s))/(t+1)


t_span = np.linspace(0, 2*np.pi, 10)
s0 = 0
# Runge-Kutta method
t, s = my_RK4(f, t_span, s0)
sol = solve_ivp(f, [0, 2*np.pi], [s0], t_eval=t)

# plot diagram
plt.figure()
plt.plot(t, s, color='red', label='RK4')
plt.plot(sol.t, sol.y[0], 'b--', label='Python Solver')
plt.xlabel("t")
plt.ylabel("f(t)")
plt.legend()
plt.grid()
plt.show()
