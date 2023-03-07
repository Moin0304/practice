# 20.Define sample code to achieve the following OOPs concepts

# •Inheritance
# •Method Overriding
# •Encapsulation
# •Method overloading
# •Abstraction

# •Inheritance
class vehicle:
    def __init__(self,make,model,year,weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight

class car(vehicle):
    def __init__(self,make,model,year,weight,num_doors):
        super().__init__(make,model,year,weight)
        self.num_doors =num_doors

    def drive():
        print('driver is driving a car ')

class truck(vehicle):
    def __init__(self,make,model,year,weight,payload_capacity):
        super().__init__(make,model,year,weight)
        self.payload = payload_capacity

    def load(self, weight):
        if weight > self.payload_capacity:
            print("Cannot load more weight than payload capacity.")
        else:
            print("Loaded {} pounds of cargo.".format(weight))

v = truck('suzuki','desire',2023,'50kg','1ton')
print(v.model)

# •Method Overriding
class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print("Generic animal sound")
        
class Dog(Animal):
    def speak(self):
        print("Woof!")
        
class Cat(Animal):
    def speak(self):
        print("Meow!")
        
animals = [Dog("Fido"), Cat("Whiskers")]
for animal in animals:
    animal.speak()


# •Encapsulation
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
        
    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount
            
    def get_balance(self):
        return self.__balance
    
account = BankAccount("1234567890", 1000)
account.deposit(500)
account.withdraw(2000)
print(account.get_balance())


# •Method overloading
class MyClass:
    def my_method(self, *args):
        if len(args) == 1:
            print("One argument:", args[0])
        elif len(args) == 2:
            print("Two arguments:", args[0], args[1])
        elif len(args) == 3:
            print("Three arguments:", args[0], args[1], args[2])
        else:
            print("Invalid number of arguments")

obj = MyClass()
obj.my_method(1)
obj.my_method(1, 2)
obj.my_method(1, 2, 3)
obj.my_method(1, 2, 3, 4)

class myclass:
    def my_method(self,*args):
        return args
c = myclass()
print(c.my_method(1,2,3,4))
print(c.my_method(12,3))

# •Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

c = Circle(10)
print(c.area())
print(c.perimeter())
r = Rectangle(4,5)
print(r.area())