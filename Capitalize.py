#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    names = str(s).split(" ")
    full_name = ""
    for name in names:
        if(len(name)!=0 and name[0].isalpha()):
            name = name[0].upper() + name[1:]
            
        full_name +=name + " " 

    return full_name  
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
