# 23.Print the following pattern :

n = int(input('enter a number: '))
for i in range(n+1):
    for j in range(n-i):
        print(' ',end='')
    print('*', end='')
    print('-' * (2*i -1), end='')
    if i:
        print('*', end='')
    print()


# num = int(input("Enter the number : "))
# r = 1
# for i in range(1,num+1):
#     if i != 1:
#         print(" "*(num-i)+"*"+"-"*r+"*")
#         r += 2
#     else:
#         print(" "*(num-i)+"*")