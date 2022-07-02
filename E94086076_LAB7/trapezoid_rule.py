import numpy as np
import matplotlib.pyplot as plt
from math import floor

# separate a~b to n steps
a = -2  # define a
b = 4  # define b


def trapezoid(n_step):
    n = n_step  # difine n
    h = (b - a) / (n - 1)  # difine h
    x = np.linspace(a, b, n)  # define grid

    # define function

    def function(x):
        f = 4*(x**2) + (1/3)*x + 5
        return f

    # let f = f(x)
    f = function(x)

    # compute the integration of trapezoid and error of its
    # integration of trapezoid
    I_trap = (h/2)*(f[0] + 2 * sum(f[1:n-1]) + f[n-1])
    I_trap = floor(I_trap*1000)/1000
    # error
    err_trap = np.around((128 - I_trap), decimals=3)
    print('I_trap: ', I_trap)
    print('err_trap:', err_trap)

    x_curve = np.linspace(a, b, 1000)
    # plot diagram
    plt.figure(figsize=(12, 8))  # render background
    plt.plot(x_curve, function(x_curve), linewidth=2, c='r')  # plot red curve
    # fill color in every grid
    for i in range(len(x) - 1):
        # take four angles of the trapezoid
        # which are: (x, y) = (x(i), 0), (x(i), f(i)), (x(i+1), 0), (x(i+1), f(i+1))
        x_fill = [x[i], x[i], x[i + 1], x[i + 1]]
        y_fill = [0, f[i], f[i + 1], 0]
        color = ['darkorange', 'forestgreen', 'royalblue']
        plt.fill(x_fill, y_fill, color=color[i % 3], alpha=0.5)
    # show diagram
    plt.show()


# run tests
trapezoid(3)
trapezoid(11)
trapezoid(21)
