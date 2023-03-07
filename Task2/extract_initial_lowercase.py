#write a program to extract the words starting with lowercase letter present in the list
list = ['Nissan','maruti','hyundai','Volkswagen','audi']
lowercase = []
capitalize = []
for i in list:
    if i[0].islower():
        lowercase.append(i)
    else:
        capitalize.append(i)

print(lowercase)
print(capitalize)
    
