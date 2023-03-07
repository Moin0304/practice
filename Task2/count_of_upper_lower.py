# In a given string- 'MsYs TecHNOlogiEs iS a gREat place To woRk'
# find the count of lowercase n uppercase

# 1st Approach

def count_upper_lower(string):
    upper = 0
    lower = 0
    space = 0
    for i in range(len(string)):
        if string[i].isupper():
            upper += 1
            

        elif string[i].islower():
            lower += 1
            
        elif string[i]==" ":
            space += 1
    return lower , upper ,space

string = 'MsYs TecHNOlogiEs iS a gREat place To woRk'
count = count_upper_lower(string)
print(count)
print()


# 2nd Approach

string = 'MsYs TecHNOlogiEs iS a gREat place To woRk'
upper = 0
lower = 0
space = 0
for i in range(len(string)):
    if string[i].isupper():
        upper += 1
    elif string[i].islower():
        lower += 1
    elif string[i]==" ":
        space += 1
print(lower)
print(upper)
print(space)