# 28.Define division logic which should also handle the the scenario if input argument (second argument) is 0, 
# Use the decorator concept to include this validation before proceeding further on the actual functionality

def check_zero_division(func):
    def wrapper(a,b):
        if b == 0:
            return 'we cannot divide the number with zero ,enter the proper divisor :('
        else:
            return func(a,b)
    
    return wrapper

@check_zero_division
def divide(num1,num2):
    num = num1//num2
    return num

# divide  = check_zero_division(divide) 
print(divide(10,0))
