"""
table= [['x' if col==row else "Even" if (col*row)%2==0 else "Odd" for col in range(1,4)] for row in range(1,4)]
for row in table:
    print(row)

def fibonacci(n=2):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

print(fibonacci(8))

"""