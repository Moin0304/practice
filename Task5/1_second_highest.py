# 1.Write a program in Python to find second highest number in an integer array without using inbuilt functions.

def second_highest(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i] > l[j]:
                l[i],l[j] = l[j],l[i]
    return l[-2]


list = eval(input("enter a list: " ))
print(second_highest(list))

