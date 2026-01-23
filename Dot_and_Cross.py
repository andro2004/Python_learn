#You are given two arrays A and B . Both have dimensions of N X N.
#Your task is to compute their matrix product.


n = int( input())


import numpy as np

A = []
for i in range (0,n):
    nums = input().split(" ")
    for i in nums:
        A.append(int(i))
B = []
for i in range (0,n):
    nums = input().split(" ")
    for i in nums:
        B.append(int(i))

A = np.array(A).reshape(n,n)
B = np.array(B).reshape(n,n)

C = np.dot(A,B)

print (C)