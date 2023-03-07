c=(i*i for i in range(5))
print(c)

def myfunction():
    print('1st function')
    yield 10
    print('2nd function')
    yield 20
    print('3rd function')
    yield 30
fun = myfunction()

# print(next(fun))
# print(next(fun))
# print()


for i in fun:
    print(i)

