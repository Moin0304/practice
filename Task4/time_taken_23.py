# 23.Write a logic for calculating the time taken for executing the python function

import time

start = time.time()
def calculate():
    print('hello world')
end = time.time()

time_taken = end - start
print(time_taken)
calculate()