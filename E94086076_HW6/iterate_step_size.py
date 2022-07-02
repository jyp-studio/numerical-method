import numpy as np
from my_central_diff import my_central_diff
import matplotlib.pyplot as plt
plt.style.use("seaborn-poster")


# define step size
h = 1
# define number of iterations to perform
iterations = 15
# list to store our step sizes
step_size = []
# list to store max error for each step size
max_error = []


for i in range(iterations):
    # halve the step size
    h /= 2
    # store this step size
    step_size.append(h)
    # compute new grid
    x = np.arange(0, 2 * np.pi, h)
    # compute function value at grid
    y = np.cos(x)
    # compute vector of forward differences
    central_diff = my_central_diff(y) / (2 * h)
    # compute corresponding grid
    x_diff = x[1:-1]
    # compute exact solution
    exact_solution = -np.sin(x_diff)
    # Compute max error between
    # numerical derivative and exact solution
    max_error.append(max(abs(exact_solution - central_diff)))
    # produce log-log plot of max error versus step size
plt.figure(figsize=(12, 8))
plt.loglog(step_size, max_error, "v")
plt.xlabel('step size')
plt.ylabel('max error')
plt.show()
