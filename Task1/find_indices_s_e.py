# 26. You are given a string S. Your task is to find the indices of the start and end of string k in S
#The first line contains the string S.The second line contains the string k.
#Print the tuple in this format: (start _index, end _index). If no match is found, print (-1,-1).

#Sample Input Sample Output
#aaadaa     (0, 1)
#aa         (1, 2)
#           (4, 5)


import re

String = input("enter a string: ")
substring = input("enter a string: ")

pattern = re.compile(substring)
match = pattern.search(String)

if not match: 
    print('(-1, -1)')
    
while match:
    print('({0}, {1})'.format(match.start(), match.end() - 1))
    match = pattern.search(String, match.start() + 1)


s = input("enter a string:")
x = re.findall("aa",s)
print(x)