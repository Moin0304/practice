# 1.Write a program in which two strings are given and determine if they share a common substring.
#  A substring may be as small as one character.  The function returns either “YES” or “NO”.


def common_string(string,substring):
    if substring in string:
        return "Yes"
    else:
        return "No"
string = input("enter a main string: ")
substring = input("enter a substring: ")
print(common_string(string,substring))