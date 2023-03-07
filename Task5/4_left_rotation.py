# 4.Write Python program to perform left rotation of array elements by two positions.

def left_rotation(list):
    left = int(input('enter a number: '))
    l1 = l[left:]+l[:left]
    return l1 
l = eval(input('enter a list: '))
print(left_rotation(l))