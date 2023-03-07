# 3.Write Python Program to delete element from array at given index.


def delete_element(list):
    l1 =[]
    index = int(input('enter index to remove element: '))
    for i in range(len(l)):
        if i==index:
            continue
        l1.append(l[i])
    return l1
l = eval(input('enter a list: '))
print(delete_element(l))