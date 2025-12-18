#You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.

####solution####

import numpy as np
arr = input().strip().split(' ')

arr3x3 = np.array(arr,int).reshape(3,3)
print(arr3x3)
