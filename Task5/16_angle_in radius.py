# 16.Write a function in Python that accepts one numeric parameter. 
# This parameter will be the measure of an angle in radians. 
# The function should convert the radians into degrees and then return that value. 
# Do not use inbuilt functions.
# Note : Angle in Radians × 180°/π = Angle in Degrees.

def angle_in_degrees(radius):
    in_degree = radius * 180 /3.14
    return in_degree
rad = int(input('enter the radius: '))
print(angle_in_degrees(rad))