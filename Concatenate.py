

#You are given two integer arrays of size N X P and M X P (N & M  are rows, and P  is the column).
# Your task is to concatenate the arrays along axis .
####solutioln###
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
arr = input().strip().split(' ')


for i in range(len(arr)):
    arr[i] = int(arr[i])
array_tuple=()
rows = arr[0]+arr[1]
cols = arr[2]
for i in range(rows):
    input_arr = input().strip().split(' ')
    for i in range(len(input_arr)):
      input_arr[i] = int(input_arr[i])
    array_tuple+=(np.array(input_arr),)

print (np.concatenate(array_tuple).reshape(rows,cols)  ) 

    

    