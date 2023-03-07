# 13. Write a python program to take 2 inputs(numbers) from user. 
# Divide the greater number by the smaller number. 
# Validate the user inputs, it should be integer type only . If the input is not integer,
#  raise exception and catch it. Also, if divisor is 0, 
# catch the exception raised.

def exception(a,b):
    try:
        if num2 == 0:
            raise ZeroDivisionError
        result = num1 / num2 if num1 > num2 else num2 / num1
        print("Result of division:", result)
    except ValueError:
        print("Invalid input: Please enter integers only")
    except ZeroDivisionError:
        print("Invalid input: Cannot divide by zero")

num1 = int(input("Enter first integer number: "))
num2 = int(input("Enter second integer number: "))

exception(num1,num2)