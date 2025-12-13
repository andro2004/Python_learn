#Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer.
# Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to.
# Here,. Please use list comprehensions rather than

#####solution:
if __name__ == '__main__':
    print ("Enter x:")
    x = int(input())
    print ("Enter y:")
    y = int(input())
    print ("Enter z:")
    z = int(input())
    print ("Enter n:")
    n = int(input())
    
#    temp = [x,y,z]
    coordinates =[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if (i+j+k)!=n:
                    coordinates.append([i,j,k])

    print(coordinates)