# 26.Print the pattern Pattern for the input : 3
# *1 
# 21*
# *123

# Note : Logic should also work for dynamic input - Ex: 5

n = int(input('enter a number: '))
s = "*"

for i in range(1,n+1):
    if i%2!=0:
        s += str(i)
        print(s)
    else:
        s += str(i)
        r = s[::-1]
        print(r)