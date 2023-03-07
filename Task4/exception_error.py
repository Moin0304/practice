# 18.Write sample code for reproducing the below errors and print the user defined messages 
# with the use of exception handling concept

# •IndexError,TypeError,AttributeError,ValueError



# IndexError example
try:
    a = [1, 2, 3]
    print(a[3])
except IndexError:
    print("Error: index out of range")

# TypeError example
try:
    a = "hello"
    b = a + 5
except TypeError:
    print("Error: unsupported operand type(s) for +")

# AttributeError example
try:
    a = 10
    a.append(5)
except AttributeError:
    print("Error: 'int' object has no attribute 'append'")

# ValueError example
try:
    a = int("hello")
except ValueError:
    print("Error: invalid literal for int()")
