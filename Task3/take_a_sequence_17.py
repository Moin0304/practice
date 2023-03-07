# 17.Write a function that takes a sequence (like a list, string, or tuple) and a number n and
#  returns the last n elements from the given sequence, as a list. For example:
# >>> tail([1, 2, 3, 4, 5], 3)

# [3, 4, 5]

def sequence(l,n):
    return l[n-1:]
l=[1, 2, 3, 4, 5]
n = int(input("enter a number: "))
print(sequence(l,n))
