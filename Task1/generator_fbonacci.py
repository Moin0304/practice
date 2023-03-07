import unittest

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a 
        a, b = b, a + b
fib = fibonacci(10)
print(fib)
for i in fib:
    print(i,end=" ")


# class TestFibonacci(unittest.TestCase):
#     def test_fibonacci(self):
#         # Test the first 10 Fibonacci numbers
#         expected_output = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#         fib = fibonacci(10)
#         for i, val in enumerate(fib):
#             self.assertEqual(val, expected_output[i])

# if __name__ == '__main__':
#     unittest.main()