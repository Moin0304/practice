# 2.Define a function which returns a list contains only the palindrome strings from the list of provided string elements
# input	: List of strings
# output : List of palindrome strings

def list_of_palindrome(list):
    l = []
    for i in list:
        if i == i[::-1]:
            l.append(i)
    return l
list = ['mom','dad','pop','top']
print(list_of_palindrome(list))
