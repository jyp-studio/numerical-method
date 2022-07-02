import numpy as np

# error
error = 0.0001

# test values
a = np.array([[8, 4, -3], [-2, -8, 5], [3, 5, 10]])
y = np.array([14, 5, -8])
a1 = np.array([[12, 3, -5], [1, 5, 3], [3, 7, 13]])
y1 = np.array([10, 6, 3])
input_list = [a, a1, y, y1]


def gauss_seidel(a_matrix, y_matrix):
    '''solving final x_matrix by gauss_seidel'''
    # initialization
    rows, columns = a_matrix.shape  # get a_matrix's shape
    x_matrix = np.zeros(shape=(rows, 1), dtype=float)  # zero matrix
    last_x_matrix = np.ones(shape=(rows, 1), dtype=float)  # ones matrix
    counter = 1  # counter

    print('Iteration results')
    print(" k,   x1,    x2,      x3")

    while any(abs(x_matrix - last_x_matrix) >= error):
        # initialize boundary condition: last_x_matrix
        last_x_matrix = np.array(x_matrix)
        for i in range(rows):
            # first find sum
            sum = 0
            for j in range(columns):
                # if i != j, add it to sum
                if i != j:
                    sum += a_matrix[i][j] * x_matrix[j]
                else:
                    continue
            # do gauss_seidei method round to the 4th decimal place
            x_matrix[i] = np.around(((y_matrix[i] - sum) / a_matrix[i][i]), 4)

        # print counter
        print('{:>2}'.format(counter), end=' ')

        # print items in x_matrix
        for item in x_matrix:
            print('{:>7.4f}'.format(item[0]), end='  ')
        print()  # go to next line

        # counter = counter + 1
        counter += 1

    # finish looping
    print('Converged!')


# run sample
for i in range(2):
    print('Sample', i + 1)
    x_list = gauss_seidel(input_list[i], input_list[i + 2])
    print('------------------------------')
