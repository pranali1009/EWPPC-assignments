import numpy as np

matrix1 = np.matrix([
    [1,2,3,4],
    [5,6,7,8]
])
matrix2 = np.matrix([
    [7,8],
    [9,10],
    [11,12],
    [13,14]
])

print(matrix1 * matrix2)