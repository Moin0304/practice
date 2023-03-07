# 14. In the given list, check if the element is None, replace it with the recent value .
# l = [1,None,None,3,None,4] Output should be : [1,1,1,3,3,4]


def replace_none_recent_value(list):
    for i in range(len(list)):
        if list[i] == None:
            list[i] = list[i-1]
    return list

l = [1,None,None,3,None,4]
print(replace_none_recent_value(l))