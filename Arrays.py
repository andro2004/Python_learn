#The NumPy (Numeric Python) package helps us manipulate large arrays and matrices of numeric data.
#To use the NumPy module, we need to import it using: import numpy

####solution#####

import numpy
def arrays(arr):
    # complete this function
    # use numpy.array
    new_arr =[]
    for i in range(len(arr)):
        new_arr.append(arr[len(arr)-1-i])
    
    return numpy.array(new_arr,float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)