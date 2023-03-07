# Find the highest sum of the string by removing the duplicates for each iteration
# input=’1211’

def highest(string):
    n = ""
    sum = 0
    for i in string:
        if i not in n:
            n += i
            sum += int(i)
    return sum  
print(highest("12211"))



