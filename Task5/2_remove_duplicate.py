# 2.Write a program in Python to remove duplicate elements form array without using inbuilt function.

def remove_duplicate(list):
    l1 = []
    for i in range(len(l)):
        if l[i] not in l1:
            l1.append(l[i])
    return l1
l = [ 1,2,3,4,2,3]
print(remove_duplicate(l))