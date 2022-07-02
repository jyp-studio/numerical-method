import copy
from typing import Union, Tuple


# here one can change matrices' values
a = [[2, 3], [4, 6]]
b = [[1, 2, 1], [3, 4, 4]]


def matrix_add(matrix_a: list, matrix_b: list) -> Tuple[bool, Union[list, None]]:
    '''The function add two matrices and return (True, answer(list))
       if the matrices are addible else return (False, None)'''
    
    # calculate the dimension with row_counter and column_counter
    row_counter = 0
    column_counter = 0

    # counting matrix_a's dimension
    for row in range(len(matrix_a)):
        row_counter += 1
    for row_item in range(len(matrix_a[0])):
        column_counter += 1
    
    # counting matrix_b's dimension
    for row in range(len(matrix_b)):
        row_counter -= 1
    for row_item in range(len(matrix_b[0])):
        column_counter -= 1

    # Since we increased row/column counter when computing matrix_a and 
    # decreased row/column counter when computing matrix_b; 
    # therefore, if either row or column counter isn't 0 
    # means that the dimension of two matrices are not equal 
    if row_counter != 0 or column_counter != 0:
        return False, None
    else:
        # shallow copy will change matrix_a too
        matrix_c = copy.deepcopy(matrix_a)
        # add two matrices
        for row in range(len(matrix_b)):
            for row_item in range(len(matrix_b[row])):
                matrix_c[row][row_item] += matrix_b[row][row_item]
        return True, matrix_c

# if a and b is addible then calculate the answer else return they are not computatible.
addible, matrix_c = matrix_add(a, b)
print(matrix_c) if addible else print("Matrix dimensions are not computatible for addition.")
