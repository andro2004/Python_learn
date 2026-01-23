#Your task is to print an array of size N X M with its main diagonal elements as 1's and 0's everywhere else.


###solution###
import numpy as np
np.set_printoptions(legacy='1.13')
dims = input().split(" ")

for i in range (0,2):
    dims[i] = int(dims[i])

mat = np.eye(dims[0], dims[1], dtype=float)
print(mat)