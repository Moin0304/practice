#13. Write a lambda function which takes two input arguments x and y. If x is greater than y then it
#should return square of y and if y is greater than x, then it should return square of x.

square = lambda x,y:y**2 if x>y else x**2
print(square(2,3))