# 10.Generate a dictionary from the two given lists using dict function (without using for loops) 
# and calculate the sum of all the values in the dictionary using reduce and anonymous concepts
# L1 = [“a”,”b”]	L2 = [1,2]

# Expected Output :
# data = {“a'.1, “b'.2} sum = 3

# l1 = ['a','b']
# l2 = [1,2]
# d = {}
# print(d.fromkeys(l1,None))

from functools import reduce

L1 = ['a', 'b']
L2 = [1, 2]

data = dict(zip(L1, L2))
print("Dictionary:", data)

sum_of_values = reduce(lambda x, y: x + y, data.values())
print("Sum of values:", sum_of_values)
