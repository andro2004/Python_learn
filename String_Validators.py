#You are given a string S.
#Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

#In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
#In the second line, print True if  has any alphabetical characters. Otherwise, print False.
#In the third line, print True if  has any digits. Otherwise, print False.
#In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
#In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

###solution###
if __name__ == '__main__':
    s = input()

    alphanumeric=False
    alphabetical=False
    digits=False
    lowercase=False
    uppercase=False
    
    for c in s:
        if c.isalnum():
            alphanumeric = True
        if c.isalpha():
            alphabetical = True
        if c.isdigit():
            digits = True
        if c.islower():
            lowercase = True
        if c.isupper():
            uppercase = True
    
    print(alphanumeric)
    print(alphabetical)
    print(digits)
    print(lowercase)
    print(uppercase)

    
