#Given an integer,n , print the following values for each integer 1 from  to n :

#Decimal
#Octal
#Hexadecimal (capitalized)
#Binary

###solution###
def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        width = len(format(number, 'b'))
        print(
            str(i).rjust(width),
            format(i, 'o').rjust(width),
            format(i, 'X').rjust(width),
            format(i, 'b').rjust(width)
        )
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)