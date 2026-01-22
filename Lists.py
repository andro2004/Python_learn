#Consider a list (list = []). You can perform the following commands:
#insert i e: Insert integer  at position .
#print: Print the list.
#remove e: Delete the first occurrence of integer .
#append e: Insert integer  at the end of the list.
#sort: Sort the list.
#pop: Pop the last element from the list.
#reverse: Reverse the list.
#Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.


######solution###
if __name__ == '__main__':
    N = int(input())
    l = []
    for n in range(N):
        input_text = input()
        parts = input_text.split(" ")
        if(parts[0]=='insert'):
            l.insert(int(parts[1]),int(parts[2]))
        elif(parts[0]=='print'):
            print(l)
        elif(parts[0]=='remove'):
            l.remove(int(parts[1]))
        elif(parts[0]=='append'):
            l.append(int(parts[1]))
        elif(parts[0]=='sort'):
            l.sort()
        elif(parts[0]=='pop'):
            l.pop()
        elif(parts[0]=='reverse'):
            l.reverse()
