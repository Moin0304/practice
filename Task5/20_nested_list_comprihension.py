# 20.Use a nested list comprehension to find all of the numbers from 1-1000 
# that are divisible by any single digit besides 1 (2-9)

# List = [num for num in range(1,1000) if all(num%i==0 for i in range(2,9))]
# print(List)


# lst = [Num for Num in range(1,1001) if sum(Num%i==0 for i in range(2,9))>0]
# print(lst)

lst = [Num for Num in range(1,1001) if [i for i in range(2,10) if Num%i==0]]
print(lst)