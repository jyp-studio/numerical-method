import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn-poster")


def my_central_diff(y):
    '''find central diff via f'(i) = f(i + 1) - f(i - 1)
       for every i in length of y except the first and last one
    '''
    # copy y
    diff_y = np.copy(y)
    # central diff for-loop
    for i in range(1, len(y) - 1):
        diff_y[i] = (y[i + 1] - y[i - 1])
    # return diff_y that dismiss first value and last value
    return diff_y


def my_forward_diff(y):
    '''dirrerence by forward difference formula'''
    # initial a zero matrix with length(y)
    y_diff = np.zeros(len(y))
    for i in range(len(y) - 1):
        y_diff[i] = y[i + 1] - y[i]
    return y_diff


def my_num_diff_w_smoothing(x, y, n):
    '''find y_smooth and do central diff to it,
        then return y_smooth_diff and x_diff'''
    # initial a y_smooth as a zeros array
    y_smooth = np.zeros(len(y))
    # make y smooth to be y_smooth
    for i in range(n, len(y) - n+1):
        y_smooth[i] = np.mean(y[i-n:i+n])
    # find central diff of t_smooth
    h = 2*np.pi / 100  # first get step size
    y_smooth_diff = my_central_diff(y_smooth) / (2*h)
    # get x_diff's integral
    x_diff = x[n+1:-n]
    return y_smooth_diff[n+1:-n], x_diff


# random generate noisy function
np.random.seed(42)
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x) + np.random.randn(len(x))/100
[dy, X] = my_num_diff_w_smoothing(x, y, 4)
# step size
h = 2*np.pi / (100 - 1)
y_forward_diff = my_forward_diff(y) / h  # forward_diff of y

# plot noisy function
plt.figure()
plt.plot(x, y)
plt.title("Noisy Sine function")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# plot Analytic Derivative and Smoothed Derivatice
plt.figure()
plt.plot(x, np.cos(x), color='blue', label='cosine')
plt.plot(x[:-1], y_forward_diff[:-1], color='green',
         label='unsmoothed forward diff')
plt.plot(X, dy, color='red', label='smoothed')
plt.title("Analytic Derivative and Smoothed Derivatice")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
