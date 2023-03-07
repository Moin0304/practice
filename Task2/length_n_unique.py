#9. Given a list [1,2,1,5,9,10,2,2,7,5,3,10,8,9,15,17,21,16,17,90] 
# find the difference between the length of the list and the count of unique elements in the list.

list = [1,2,1,5,9,10,2,2,7,5,3,10,8,9,15,17,21,16,17,90]
length = len(list)
unique = len(set(list))

diff = length - unique
print(diff)
print(length)
print(unique)



length = 0
for i in range(len(list)):
    length += 1
    


