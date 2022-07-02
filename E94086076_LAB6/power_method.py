import numpy as np


def power_method(matrix, eignenvector) -> np.array:
    '''find eignevector and eignevalues'''
    def normalize(matrix):
        '''get the matrix's max value then div it'''
        max_eigenvalue = max(matrix, key=abs)
        normalized_eigenvector = matrix / max_eigenvalue
        # return normalized eigenvector and max eigenvalue
        return normalized_eigenvector, max_eigenvalue

    # initialize boundary condition
    last_eigenvalue = None
    eignenvalue = None
    while True:
        # get eignenvector
        eignenvector = np.dot(matrix, eignenvector).astype(float)
        # normalize
        eignenvector, eignenvalue = normalize(eignenvector)
        if last_eigenvalue == eignenvalue:
            return eignenvector, last_eigenvalue
        else:
            last_eigenvalue = eignenvalue
