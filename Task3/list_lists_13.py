
# 13.Write a function that accepts a string containing lines of numbers and returns a list of lists of numbers.
# Ex. matrix_from_string("3 4 5")
# [[3.0, 4.0, 5.0]]

def list_lists(string):
    l = []
    for i in string:
        if i.isnumeric():
            l.append(float(i))
    return [l]

string = input("enter a string: ")
print(list_lists(string))