list = [1, 2, 3, 2, 4, 2, 4, 7, 8, 4, 5, 8, 6, 9, 2]

# Create an empty dictionary
result = {}

# Loop through the list
for item in list:
    # Check if the item is even
    if item % 2 == 0:
        # Check if the item is already in the dictionary
        if item in result:
            # If it is, increment the value by 1
            result[item] += 1
        else:
            # If it's not, add it to the dictionary with a value of 1
            result[item] = 1

# Print the resulting dictionary
print(result)

list = [1, 2, 3, 2, 4, 2, 4, 7, 8, 4, 5, 8, 6, 9, 2]
result = {}
for item in list:
    if item % 2 == 0:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
print(result)