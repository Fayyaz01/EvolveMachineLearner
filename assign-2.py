import numpy as np
from numpy import matrix
A = matrix( [[1,2,3,4],[11,12,13,14],[21,22,23,24],[31,32,33,34]]) # Creates a matrix.
print(np.matrix(A.T))   # Transpose of A.
print(np.matrix(A.I))   # Inverse of A.