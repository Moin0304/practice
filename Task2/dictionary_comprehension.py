#write a program using dictionary comprehension which will contain the key value pair of i:i**2.
#value of i will start from 1 and will go upto 10

list = [x for x in range(1,11)]
print(list)
print()

dict = {x:x**2 for x in range(1,11)}
print(dict)