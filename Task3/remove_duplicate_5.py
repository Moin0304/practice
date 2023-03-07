# 5.Write a function that accepts an iterable and returns a new iterable with all items from the 
# original iterable except for duplicates.
# Ex. uniques_only([1, 2, 2, 1, 1, 3, 2, 1])
# [1, 2, 3]

# 1st Approch

def remove_duplicate(l):
    l1 = list(set(l))
    return l1

#2nd Approch

def remove_duplicate(l):
    l1 = []
    for i in l:
        if i not in l1:
            l1.append(i)
    return l1

l = [1, 2, 2, 1, 1, 3, 2, 1]
new_list = remove_duplicate(l)
print(new_list)