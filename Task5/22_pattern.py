
# 22.Print the following rhombus pattern .
# eg. If input is 4, it should print the following output .

n = int(input('enter a number: '))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end='')
    for k in range(i):
        print(i,end=' ')
    print()

for i in range(1,n):
    for j in range(i):
        print(' ',end='')
    for k in range(i+1,n+1):
        print(n-i,end=' ')
    print()


