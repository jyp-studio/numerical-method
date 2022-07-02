import numpy as np

# test values
a = np.array([[1, 2, 3], [3, 4, 5], [3, 5, 5]])
y = [2, 2, 5]

a1 = np.array([[1, 2], [3, 4]])
y1 = [2, 5]


def adjugate(matrix):
    def get_M_ij(index_0, index_1, array):
        row, column = array.shape
        M = []  # create an empty M
        for i in range(row):
            for j in range(column):
                if i == index_0 or j == index_1:  # ignore i j same with M_ij
                    pass
                else:
                    M.append([array[i][j]])  # append else
        return (np.array(M)).reshape(row - 1, column - 1)

    abj_a = np.zeros(matrix.shape)  # initial abj_a matrix
    rows, columns = abj_a.shape  # get abj_a shape
    # Loop to calculate M_ij
    for i in range(rows):
        for j in range(columns):
            minor = get_M_ij(i, j, matrix)
            abj_a[i][j] = (-1) ** (i + j) * np.linalg.det(minor)

    return abj_a.T


list = [a, a1, y, y1]  # loop two samples
for index in range(2):
    adj_a = adjugate(list[index])
    a_inverse = adj_a / np.linalg.det(list[index])  # get A'
    x = a_inverse.dot((np.array(list[index + 2])).T)

    print("adjugate matrix:")
    print(adj_a)
    print("x:")
    print(x)
