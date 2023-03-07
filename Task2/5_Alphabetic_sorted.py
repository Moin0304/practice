#Given a dictionary {‘Msys Technologies’:’Sanjay Sehgal’, ‘Infosys’:’Salil Parekh’,
#‘TCS’:’Rajesh Gopinathan’, ‘Wipro’:’Thierry Delaporte’} make a list of all the values associated
#with keys in alphabetically sorted order.

# 1st Approch

Dictionary = {'Msys Technologies':'Sanjay Sehgal', 'Infosys':'Salil Parekh','TCS':'Rajesh Gopinathan', 'Wipro':'Thierry Delaporte'}
print(sorted(Dictionary.items()))
print()
print(sorted(Dictionary.keys()))
print()
print(sorted(Dictionary.values()))
print()


# 2nd Approch

sorted_value = []
for key in sorted(Dictionary.keys()):
    print(Dictionary[key])
    sorted_value.append(Dictionary[key])

print(sorted_value)
