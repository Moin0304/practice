# 11. From the given list, check if the element is an integer then return square of that element
#  and if element is a string then return the same string 2 times. Output should be in list format.
#   a = [8,9,10,"f",5,8,"d"] 
#   Output should be :  [64, 81, 100, 'ff', 25, 64, 'dd']

def integer_square_string_repeat(list):
    l = []
    for i in list:
        if isinstance(i,int):
            l.append(i**2)
        elif isinstance(i,str):
            l.append(i+i)
    return l

a = [8,9,10,"f",5,8,"d","moin"] 
print(integer_square_string_repeat(a))