# 22.Write a function is_iterator so that it accepts an iterable and returns True 
# if the given iterable is an iterator.
# is_iterator(iter([])) True
# >>> is_iterator([1, 2]) False

def is_iterator(l):
    if l == iter(l):
        return True
    else:
        return False
l = ''
a = []
print(is_iterator(a))




# l = [1,2,3,4,5]
# print(dir(type(l)))
# print(dir(type(iter(l))))


# a = iter(l)
# for i in a:
#     print(i)
# print(next(a))





