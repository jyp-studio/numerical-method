import numpy as np
from typing import Union, Tuple


def matrix_add(a: list, b: list) -> Tuple[bool, Union[list, None]]:
    '''The function add two matrices and return (True, answer(list))
       if the matrices are addible else return (False, None)'''
    
    # initial matrix via numpy
    matrix_a = np.array(a)
    matrix_b = np.array(b)
    if matrix_a.shape != matrix_b.shape:
        return False, None
    else:
        matrix_c = matrix_a + matrix_b
        return True, matrix_c.tolist() # convert numpy format array to list and return 

# test values
# here one can change matrices' values
a = [[2, 3, 1],[4, 6, 2]] 
b = [[1, 2, 3],[3, 4, 5]] 
# if a and b is addible then calculate the answer else return they are not computatible.
addible, matrix_c = matrix_add(a, b)
print("Sample Run 1")
print(matrix_c) if addible else print("Matrix dimensions are not computatible for addition.")


# here one can change matrices' values
a = [[2, 3, 1],[4, 6, 2]]
b = [[1, 2],[3, 4]] 
# if a and b is addible then calculate the answer else return they are not computatible.
addible, matrix_c = matrix_add(a, b)
print("Sample Run 2")
print(matrix_c) if addible else print("Matrix dimensions are not computatible for addition.")


# here one can change matrices' values
a = [[2, 3, 1],[4, 6, 2]]
b = [[1, 2],[3, 4],[3, 4]]
# if a and b is addible then calculate the answer else return they are not computatible.
addible, matrix_c = matrix_add(a, b)
print("Sample Run 3")
print(matrix_c) if addible else print("Matrix dimensions are not computatible for addition.")
