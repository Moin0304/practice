
# 18.Create your own exception.

# class valid_age(Exception):
#     pass

# def check_age(age):

# def checking_age():
#     try:
#         age = int(input('enter your age: '))
#         if age > 18 :
#             print("your eligible")
#         else:
#             raise valid_age("age should be greater then 18 years")
#     except valid_age as e:
#         print(e)


# checking_age()


# class valid_age(Exception):
#     def message(self):
#         print("Hai enter the correct age please")


# def checking_age():

#     age = int(input('enter your age: '))
#     if age > 18 and age < 100:
#         print("your eligible")
#     else:
#         raise valid_age.message("age should be greater then 18 years")

# checking_age()

class CalculatorException(Exception):
    pass

class DivisionByZeroException(CalculatorException):
    def __init__(self):
        super().__init__("Division by zero is not allowed")

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise DivisionByZeroException()
        return x / y

o1 = Calculator()
print(o1.add(3,4))
print(o1.subtract(3,4))
print(o1.divide(3,0))
