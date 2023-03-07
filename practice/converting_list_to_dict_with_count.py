import collections

l = [1,2,3,4,3,4,2,6,8,6]
l1 = dict(collections.Counter(l))
print(l1)
print()



l = [1,2,3,4,3,4,2,6,8,6]
dict1 = {}
for i in l:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
print(dict1)
print()

l = [1,2,3,4,3,4,2,6,8,6]
s  = set(l)
d = {}
for i in s:
    d[i] = l.count(i)
print(d)
print()

    


    