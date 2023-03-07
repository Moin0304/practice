# def my_decorator(fun):
#     def inner_fun():
#         print("something before")
#         fun()
#         print("something after")
#     return inner_fun

# def my_function():
#     print("i am devil")

# value = my_decorator(my_function)
# value()


# def decorator(fun):
#     def deco():
#         print("hello")
#         fun()
#         print("bye")
#     return deco

# @decorator
# def greet():
#     print("moin")
# greet()

from datetime import datetime

current_day =datetime.now()
print(current_day.day)