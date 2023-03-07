# 24.Write a class that represents a circle.The circle should have a radius, a diameter, and an area. 
# It should also have a nice string representation.

class circle:
    def __init__(self,radius):
        self.radius = radius
        self.diameter = 2 * radius
        self.area = 3.14 * radius **2
c = circle(20)
print(c.area)
print(c.radius)
print(c.diameter)
