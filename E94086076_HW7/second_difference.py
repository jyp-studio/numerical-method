import numpy as np
import matplotlib.pylab as plt

# step size
h = 0.1
# define grid
x = np.arange(-2, 4, h)
# compute function
y = (1/4)*(x**4) + (1/3)*(x**3) + 5*x
# compute corresponding grid
x_diff = x[1:-1:]
# compute exact solution
exact_solution = 3*(x_diff**2) + 2*x_diff


def my_forward_diff(y):
    '''dirrerence by forward difference formula'''
    # initial a zero matrix with length(y)
    y_diff = np.zeros(len(y))
    for i in range(len(y) - 1):
        y_diff[i] = y[i + 1] - y[i]
    return y_diff


def my_backward_diff(y):
    '''dirrerence by backward difference formula'''
    # initial a zero matrix with length(y)
    y_diff = np.zeros(len(y))
    for i in range(1, len(y)):
        y_diff[i] = y[i] - y[i - 1]
    return y_diff


def sec_order_diff(y):
    '''dirrerence by second-order difference formula'''
    # initial a zero matrix with length(y)
    y_diff = np.zeros(len(y))
    for i in range(1, len(y) - 1):
        y_diff[i] = y[i + 1] - (2*y[i]) + y[i - 1]
    return y_diff


# difference of y done by forward and backward difference
y_diff_finite = (my_backward_diff(my_forward_diff(y) / h) / h)[1:-1]
# difference of y done by second difference
y_diff_second = (sec_order_diff(y) / (h**2))[1:-1]

# compute error
error_finite = abs(max((y_diff_finite - exact_solution), key=abs))
error_second = abs(max((y_diff_second - exact_solution), key=abs))
print('error of finite difference:', error_finite)
print('error of second-order:', error_second)

# plot figure
plt.figure(figsize=(12, 8))  # render background
# plot Exact solution with
# {linewidth=12, color='darkblue', label='Exact solution'}
plt.plot(x_diff, exact_solution, linewidth=12,
         c='darkblue', label='Exact solution')
# plot Finite difference approximation with
# {linewidth=5, linestyle='--', color='orange', label='Finite difference approximation'}
plt.plot(x_diff, y_diff_finite, linewidth=5, linestyle='--',
         c='orange', label='Finite difference approximation')
# plot Second-order approximation with
# {linewidth=13, color='lime', linestyle='', markerstyle='*', label='Second-order approximation'}
plt.plot(x_diff, y_diff_second, linewidth=13, c='lime',
         linestyle='', marker='*', label='Second-order approximation')
# render label with size 18
plt.legend(prop={'size': 18})
# show plot
plt.show()
