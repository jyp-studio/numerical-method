# %%
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn-poster")


def function(x):
    f = (x**3) + (x**2)
    return f


def simp_error():
    '''calculate error for each n'''
    # define grid and function
    a = -2
    b = 4
    error_list = []  # error list for error of each 'n'
    step = []
    for n in range(11, 171, 2):
        step.append(n)
        h = (b - a) / (n - 1)
        x = np.linspace(a, b, n)
        f = function(x)

        # compute error
        I_simp = (h/3) * (f[0] + 2*sum(f[:n-2:2]) + 4*sum(f[1:n-1:2]) + f[n-1])
        err_simp = abs(84 - I_simp)
        error_list.append(err_simp)

    # plot figure
    plt.figure(figsize=(12, 8))
    plt.plot(step, error_list)
    plt.xlabel("grid points")
    plt.ylabel("error")
    plt.show()
    print('minimum error:', error_list[-1])


simp_error()

# %%
