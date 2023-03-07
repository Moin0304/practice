# Define a class with a method that we want to monkey patch
class MyClass:
    def my_method(self):
        print("Original behavior")

# Define a function that we want to use to monkey patch the class method
def new_method(self):
    print("New behavior")

# Monkey patch the class method with our new method
MyClass.my_method = new_method

# Create an instance of the class and call the modified method
obj = MyClass()
obj.my_method()  # This will print "New behavior"

class Myclass:
    def my_method(self):
        print("original behavior")
def new_method(self):
    print("new behavior")

Myclass.my_method = new_method

obj = Myclass()
obj.my_method()

