import unittest


def add_version(match,input):
    result = match +str(input)
    return result

match = "version"
input = 8
print(add_version(match,input))

class test_version(unittest.TestCase):
    def test_version1(self):
        self.assertEqual(add_version("version",8),"version8")
    def test_version2(self):
        self.assertEqual(add_version("v1.",2),"v1.2")
    def test_version3(self):
        self.assertNotEqual(add_version("version",9),"version8")

if __name__== '__main__':
    unittest.main()
