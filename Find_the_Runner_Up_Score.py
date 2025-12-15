#Given the participants' score sheet for your University Sports Day
#you are required to find the runner-up score.
# You are given n scores. Store them in a list and find the score of the runner-up.

import sys

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    max1=-sys.maxsize - 1 
    max2=max1
    
    for num in arr:
        if num>max1:
            max2=max1
            max1=num
        elif num==max1:
            continue
        elif num<max1:
            if num>max2:
                max2=num

        
    print(max2) 
        
        
    
    
    