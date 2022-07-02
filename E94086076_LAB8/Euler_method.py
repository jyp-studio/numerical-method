# %%
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn-poster")


# Define parameters
def f(t, s):
    return np.exp(-2*t)  # the r.h.s of the ODE


# Numerical grid
# define time interval delta_t
delta_t = 0.1
# Numerical grid t
t = np.arange(0, 1 + delta_t, delta_t)
# Initial Condition s_0
s_0 = -1/2
# Explicit Euler Method
# define temp solution
s = np.zeros(len(t))
s[0] = s_0

# solve iteratively
for i in range(0, len(t) - 1):
    s[i + 1] = s[i] + delta_t*f(t[i], s[i])
plt.figure(figsize=(12, 8))
plt.plot(t, s, "-", label="Forward Euler Method")
plt.plot(t, (-1/2) * np.exp(-2*t), "r--", label="Exact")
plt.title("Euler v.s. Exact")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.grid()
plt.legend(loc="lower right")
plt.show()

# %%
