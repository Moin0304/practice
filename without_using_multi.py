import unittest


def multiple(a,b):
    result = 0
    if a > b :
        for i in range(a):
            result += b
    else:
        for i in range(b):
            result += a

    return result
# print(multiple(2,3))

class test_multiple(unittest.TestCase):
    def test_multiple1(self):
        self.assertEqual(multiple(10,5),50)
    def test_multiple2(self):
        self.assertEqual(multiple(66,99),6534)
    def test_multiple3(self):
        self.assertNotEqual(multiple(16,18),87)
if __name__ == '__main__' :
    unittest.main()
