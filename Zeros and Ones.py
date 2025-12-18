#You are given the shape of the array in the form of space-separated integers
#each integer representing the size of different dimensions
#your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.

#####solution####
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
arr = input().strip().split(' ')

shape_tuple = (int(arr[0]),)
for i in range(1,len(arr)):
    shape_tuple += (int(arr[i]),)
zeros = np.zeros(shape_tuple,dtype = int)
ones = np.ones(shape_tuple,dtype =int)

print(zeros)
print(ones)