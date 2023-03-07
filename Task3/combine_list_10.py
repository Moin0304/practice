# 10.Write a function combine_lists should take two lists and return a new list 
# containing all elements from both lists.

def combine_list(list1,list2):
    list = list1 + list2
    return list

list1 = [1,2,3,4,5,6]
list2 = [1,2,3,4,5,6]
print(combine_list(list1,list2))