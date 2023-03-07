# 10. Sort the list of integers in descending order without using inbuilt functions . 
# lst = [56,2,13,1,78,4,6]

def descending_order(list):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i] < list[j]:
                list[i],list[j] = list[j],list[i]

    return list

lst = [56,2,13,1,78,4,6]
print(descending_order(lst))