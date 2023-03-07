# 26.Check sum of 2 numbers from given list which matches target value and 
# returns the indexes of those numbers in the form of list.
# l1 = [ 7,8,2,3,6,9,2,8]
# Target = 14
# O/p should be: [1,4]
# Note : We should not be using more than 1 loop.

# def sum_of_2_target(l1):
#     length = len(l1)
#     for i in range(length):
#         for j in range(i+1,length):
#             if l1[i]+l1[j] == target :
#                 return i,j
# list = eval(input("enter a list: "))
# target = int(input('enter a number: '))
# print(sum_of_2_target(list))

def find_indexes(numbers, target):
    complement_dict = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if num in complement_dict:
            return [complement_dict[num], i]
        complement_dict[complement] = i
    return None
    

l1 = eval(input('enter a list: '))
target = int(input('enter a number: '))

result = find_indexes(l1, target)
print(result)



