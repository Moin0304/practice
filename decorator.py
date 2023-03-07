def capital(fun):
    def wrapper():
        return "HELLO"
    return wrapper

@capital
def print_hello():
    return "Hello"
print(print_hello())