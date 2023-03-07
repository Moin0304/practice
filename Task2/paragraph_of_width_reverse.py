# 21. You are given a string and width. Your task is to wrap the string into paragraph of width in
# reverse order. Blank spaces should be ignored.
# for eg: i/p - first line contains a string with blank spaces - Hello, welcome to this
# organisation.
# the second line conatins the width - 4
# o/p
# lleH
# ew,o
# mocl
# tote
# osih
# nagr
# tasi
# .noi

string = 'Hello, welcome to this organisation.'
width = int(input("enter a width: "))
new_string = string.replace(" ",'')
print(new_string)
l = list(new_string)
print(l)
l1 = []
for i in range(0,len(l),width):
    l1.append(l[i:i+width])

for i in l1:
    print(''.join(i[::-1]))