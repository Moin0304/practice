# 15.Write a function get_hypotenuse that returns the hypotenuse of a right triangle given the other
#  two sides.
# >>> get_hypotenuse(0, 0)
# 0.0
# >>> get_hypotenuse(3, 4)
# 5.0


def get_hypotenuse(a,b):
    return ((a**2) + (b**2))**.5


import math

def get_hypotenuse(a,b):
    return math.sqrt((a**2)+(b**2))

print(get_hypotenuse(3,4))
