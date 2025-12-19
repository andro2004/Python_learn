#We can generate the transposition of an array using the tool numpy.transpose.
#It will not affect the original array, but it will create a new array.


######solution#####
import numpy as np    

size = input().strip().split(' ')

size = [int(i) for i in size]

numbers=[]
for i in range(size[0]):
    values=input().strip().split(' ')
    values=[int(v) for v in values ]
    numbers.append(values)

numbers = np.array(numbers)
print(np.transpose(numbers))
print(numbers.flatten())