#In the dictionary {‘India’:’New Delhi’, ‘USA’:’Washington D.C.’, ‘Nepal’:’Kathmandu’} list out
#all the keys in a list named as ‘list_keys’ and list out all the values in a list named as ‘list_values’.
#Also find out the value of key ‘Australia’ in the list and as it is not existing in the list print ‘NA’ as
#its value.


# 1st Approch

Dictionary = {'India':'New Delhi', 'USA':'Washington D.C.', 'Nepal':'Kathmandu'}

list_key = Dictionary.keys()
print(list_key)
print()

list_value = Dictionary.values()
print(list_value)
print()

d = Dictionary.get('Australia','NA')
print(d)


# 2nd Approch

list_keys = []
list_values = []

for keys in Dictionary.keys():
    list_keys.append(keys)
for value in Dictionary.values():
    list_values.append(value)

print(list_keys)
print(list_values)
print(Dictionary)


# 3rd Approch

list_keys = []
list_values = []
for i,j in Dictionary.items():
    list_keys.append(i)
    list_values.append(j)
print(list_keys)
print(list_values)