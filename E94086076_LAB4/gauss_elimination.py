import numpy as np


# test values
a = np.array([[1, 2, 3, 4], [5, 4, 3, 2], [2, 1, 2, 4], [2, 1, 3, 4]])
y = np.array([4, 8, 5, 6])

# combine a and y to a matrix
y = np.reshape(y, (len(y), 1))  # reshape y
gauss_matrix = np.hstack((a, y)).astype(float)  # concate a and y


gauss_row, gauss_column = gauss_matrix.shape
# make all lower-triangle row bocomes 0 and switch to right-second column
for column in range(gauss_column - 2):  # gauss_column - y - last column
    # print("column:", column)
    for row in range(column + 1, gauss_row):  # row = column + 1
        '''
        print("row:", row)
        print(f"gauss_matrix[{row}][{column}] = {gauss_matrix[row][column]}")
        print(
            f"gauss_matrix[{column}][{column}] = {gauss_matrix[column][column]}")
        '''
        # times
        times = -(gauss_matrix[row][column] /
                  gauss_matrix[column][column])
        # print("times:", times)

        # elimination
        gauss_matrix[row] = gauss_matrix[column] * times + gauss_matrix[row]
        # print(gauss_matrix)

print("upper triangular matrix:")
print(gauss_matrix)

# make all upper-triangle row bocomes 0 and switch to left-second column
for column in range(gauss_column - 2, 0, -1):  # gauss_column - y - first column
    # print("column:", column)
    for row in range(column - 1, -1, -1):  # row = column + 1
        '''
        print("row:", row)
        print(f"gauss_matrix[{row}][{column}] = {gauss_matrix[row][column]}")
        print(
            f"gauss_matrix[{column}][{column}] = {gauss_matrix[column][column]}")
        '''
        # times
        times = -(gauss_matrix[row][column] /
                  gauss_matrix[column][column])
        # print("times:", times)

        # elimination
        gauss_matrix[row] = gauss_matrix[column] * times + gauss_matrix[row]
        # print(gauss_matrix)

# calculate answer
answer = []
for i in range(gauss_row):
    answer.append(gauss_matrix[i][gauss_column - 1] / gauss_matrix[i][i])
print("x:")
print(answer)
