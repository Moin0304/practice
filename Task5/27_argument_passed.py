# 27.For any function, find out the arguments passed in the function using in-built python module 
# and also explore on all other possible values we can get using the same python module.
# eg. def test(x1, x2, x3=10):
# pass
# Using the in-built python module, find all the arguments passed in the test function.

import inspect

def test(x1,x2,x3=10):
    pass

sig = inspect.signature(test)
print(sig.parameters.keys())