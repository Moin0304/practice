# 18. Print the below rohmbus pattern according to the given number
# for eg: given number is 4 then
# o/p will be
# 1
# 212
# 32123
# 4321234
# 32123
# 212
# 1

# n = int(input("enter a number: "))
# for i in range(n):
#     for j in range(i+i+1):
#         print("*",end='')
#     for k in range(i+i+1,n):
#         print('',end="")
#     print()

# for l in range(n-1,0,-1):
#     for m in range(l+l-1):
#         print("*",end='')
#     for n in range(n):
#         print('',end='')
#     print()
    

# n = int(input("enter a number: "))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end='')
#     for j in range(i+i+1):
#         print("*",end='')
#     print()
    
# for l in range(1,n):
#     for m in range(l):
#         print(" ",end='')
#     for n in range((n+l)//l):
#         print("*",end='')
#     print()

n = int(input("enter a number: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end='')
    for j in range(i,0,-1):
        print(j,end='')
    for j in range(2,i+1):
        print(j,end='')
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end='')
    for j in range(i,0,-1):
        print(j,end='')
    for j in range(2,i+1):
        print(j,end='')
    print()
    
