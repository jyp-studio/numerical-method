import numpy as np


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
    return diff_y[1:-1]
