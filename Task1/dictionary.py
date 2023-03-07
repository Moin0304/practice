import collections


list = [1, 2, 3, 2, 4, 2, 4, 7, 8, 4, 5, 8, 6, 9, 2]
res = dict(collections.Counter(list))
print(res)

list = [1, 2, 3, 2, 4, 2, 4, 7, 8, 4, 5, 8, 6, 9, 2]
result = {}
for item in list:
    if item % 2 == 0:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
print(result)