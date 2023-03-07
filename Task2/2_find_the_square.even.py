# Given a list of first 10 natural numbers, write a program to find the square of all even numbers
# and cube of all odd numbers and store them in another list

# 1st Approch

natural_numbers = [1,2,3,4,5,6,7,8,9,10]
list1 = []
print(list)
for i in natural_numbers:
    if i % 2 ==0:
        list1.append(i**2)
    else:
        list1.append(i**3)
print(list1)
print()

# 2nd Approach

square = list(map(lambda x:x**2 ,natural_numbers))
cube = list(map(lambda x: x**3,natural_numbers))
print(square)
print(cube)
print()
# print()

# 3rd Approach
square_cube = list(map(lambda x : x**2 if x%2 == 0 else x**3,natural_numbers))
print(square_cube)