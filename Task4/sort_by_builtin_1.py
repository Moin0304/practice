# 1.Sort the below list without using inbuilt function I = [2,3,-5,-7,9,4,6,-1,-8,0]



def sorting_list(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i] > l[j]:
                l[i],l[j] = l[j],l[i]
    return l
l = [2,3,-5,-7,9,4,6,-1,-8,0]
print(sorting_list(l))
