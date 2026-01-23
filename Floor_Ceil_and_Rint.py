#You are given a 1-D array,A.
#Your task is to print the Floor, Ceil and Rint of all the elements of A.

###solution###

import numpy as np
np.set_printoptions(legacy ='1.13')

nums = input().split(" ")

numbers = []
for n in nums:
    numbers.append(float(n))

numbers = np.array(numbers)
print(np.floor(numbers))
print(np.ceil(numbers))
print(np.rint(numbers))