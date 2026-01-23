#You are given a 2-D array with dimensions N X M.
#Your task is to perform the min function over axis 1 and then find the max of that.


###solution###


import numpy as np
dims = input().split(" ")

for i in range (0,2):
    dims[i] = int(dims[i])

numbers = []
for i in range (0,dims[0]):
    nums = input().split(" ")
    for n in nums:
        numbers.append(int(n))

numbers = np.array(numbers).reshape(dims[0],dims[1])
numbers = np.min(numbers, axis = 1)
numbers = np.max(numbers)
print(numbers)