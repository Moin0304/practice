# 3.Write a function called interleave which accepts two iterables of any type and returns a new iterable
#  with each of the given items "interleaved" (item 0 from iterable 1, then item 0 from iterable 2,
#  then item 1 from iterable 1, and so on).An assumption here that both iterables contain 
#  the same number of elements.

def interleave(l1,t1):
    l = []
    if len(l1) == len(t1):
        for item1,item2 in zip(l1,t1):
            l.append(item1)
            l.append(item2)
    else:
        return "the length of the l1 and t1 are not equal"
    return l

l1 = [1,2,3,4,5,6]
t1 = ["a","b","c","d","e","f"]
print(interleave(l1,t1))