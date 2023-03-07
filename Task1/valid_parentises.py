#Write a Python class to check the validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
#These brackets must be closed in the correct order, for example "()" and "()[]{}" are valid
#but "[)", "({[)]" and "{{{" are invalid

def validity(string):
    stack = []
    paranthises = ["()","[]","{}"]
    open_parenthises = ['(','[','{']
    for i in string:
        if i in open_parenthises:
            stack.append(i)
        else:
            if stack.pop() + i not in paranthises:
                return "its not a valid parenthises"
    if len(stack) == 0:
        return "its valid parenthises"
    else:
        return "its not valid parenthises"

string = input("enter parentheses: ")
print(validity(string))
            
                