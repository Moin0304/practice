#printing odd numbers

li = [1,2,3,4,5,6,7]
li1 = li[::2]
print(li1)

res=[]
for i in li:
    if i % 2 != 0:
        res.append(i)
print(res)

result = []
for i in range(1,len(li)+1,2):
    result.append(i)
print(result)


l = [ x for x in li if x%2 != 0]
print(l)

l1 = list(filter(lambda a : a%2 != 0,li))
print(l1)


