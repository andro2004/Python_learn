#You are given a 2-D array with dimensions N X M.
#Your task is to perform the sum tool over axis 0 and then find the product of that result.


###solution###


import numpy as np
dims = input().split(" ")

for i in range (0,2):
    dims[i] = int(dims[i])

numbers = []
for i in range (0,dims[1]):
    nums = input().split(" ")
    for n in nums:
        numbers.append(int(n))

numbers = np.array(numbers).reshape(dims[0],dims[1])
numbers = np.sum(numbers, axis = 0)
numbers = np.prod(numbers)
print(numbers)