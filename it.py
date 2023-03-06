# my_list = [1, 2, 3, 4, 5]
# my_iterator = iter(my_list)

# while True:
#     try:
#         item = next(my_iterator)
#         print(item)
#     except StopIteration:
#         break


def fibonacci(n):
    """Generate the first n Fibonacci numbers."""
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
for num in fibonacci(10):
    print(num)

