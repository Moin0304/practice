# 30.Create below 3 functions :
# -function 1 calculates sqrt
# -function 2 calculates cube

# -function 3 calculates square
# Pass 50,00,000 as an integer argument which is going to be used as a range of integers.
# Call above 3 functions in parallel using below 3 ways :
# 1)Using multiprocessing
# 2)Using threading.thread
# 3)Using threadpoolexecutor
# Calculate the total time taken in each of these 3 ways .
#  Share your observations/insights on the results obtained.

def sqrt(num):
    return num ** 0.5

def cube(num):
    return num**3

def square(num):
    return num**2

n = 25
print(sqrt(n))
print(cube(n))
print(square(n))