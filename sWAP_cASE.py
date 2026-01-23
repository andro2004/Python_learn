#You are given a string and your task is to swap cases.
#In other words, convert all lowercase letters to uppercase letters and vice versa.


###solution###
def swap_case(s):
    result =""
    for c in s:
        if c.isalpha():
            if c.islower():
                result +=c.upper()
            else:
                result +=c.lower()
        else:
            result += c;
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)