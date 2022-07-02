import numpy as np
from my_central_diff import my_central_diff
import matplotlib.pyplot as plt
plt.style.use("seaborn-poster")

# step size
h = 0.1
# define grid
x = np.arange(0, 2*np.pi, h)
# compute function
y = np.cos(x)


# central differences
central_diff = my_central_diff(y) / (2*h)
# compute corresponding grid
x_diff = x[1:-1]
# compute exact solution
exact_solution = -np.sin(x_diff)

# plot solution
plt.figure(figsize=(12, 8))  # render background
plt.plot(x_diff, central_diff, linewidth=8,
         label="Finite difference approximation")
plt.plot(x_diff, exact_solution, linewidth=4, label="Exact solution")
plt.legend()  # show label
plt.show()

# Compute max error between
# numerical derivative and exact solution
max_error = max(abs(exact_solution - central_diff))
print('The maximum error is', max_error)
