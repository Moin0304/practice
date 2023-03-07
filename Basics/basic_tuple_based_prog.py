#Write a Python program to create a tuple with elements in reverse order

def tuple(t):
    reverse = t[::-1]
    return reverse
t=(1,2,3,4,5,6)
print(tuple(t))

#Write a Python program to find the length of a tuple

print(len(t))

#Write a Python program to find the maximum and minimum element of a tuple.

print(max(t))
print(min(t))

#Write a Python program to find the sum of all elements in a tuple
a =0
for i in t:
    a += i
print(a)

#Write a Python program to find the number of occurrences of a given element in a tuple.

def tuple(t,ele):
    count = 0
    for i in t:
        if i == ele:
            count += 1
    return count
t = (1,2,3,4,5,6,7,8,2,3,4)
ele = 2
print(tuple(t,ele))

#Write a Python program to convert a tuple to a string.

def tuple_to_string(t):
    string = ""
    for i in t:
        string += str(i)
    return string
t = (1,2,3,4,5,6)
print(tuple_to_string(t))

#Write a Python program to check if an element exists in a tuple

def element(t,ele):
    if ele in t:
        return True
    else:
        return False
t = (1,2,3,4,5,6)
ele = 6
print(element(t,ele))

#Write a Python program to concatenate two tuple

def cancatenate(t1,t2):
    t3 = t1 + t2
    return t3
t1 = (1,2,3,4,5)
t2 = (6,7,8,9,0)
print(cancatenate(t1,t2))

#Write a Python program to slice a tuple.

def slice(t):
    t1 = t[1:3]
    return t1
t = (1,2,3,4,5,6)
print(slice(t))




