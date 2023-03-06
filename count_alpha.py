# Write a program to find the count of alphabet alone in the given alphanumeric string for
#Ex1: input=’abb24ccc8ddbbca1’ output=’a1b224c3d2b2c1a11’
#Ex2: input = ‘abc23’ output=’a1b1c123’
import unittest

def alpha(string):
    length = len(input)
    result = ""
    count = 0
    temp = 0
    index = 0
    while index < length:
        if not input[index].isdigit():
            temp = index
            while temp < length:
                if input[index] == input[temp]:
                    count += 1
                    temp += 1
                else:
                    break
            result += input[index] + str(count)
            count = 0
            index = temp
        else:
            result += input[index]
            index += 1
    return result

input = "abc23"
print(alpha(input))

# class test_alpha(unittest.TestCase):
#     def test_count_alpha1(self):
#         self.assertEqual(alpha("abc23"),"a1b1c123")
#     def test_count_alpha2(self):
#         self.assertEqual(alpha("abb24ccc8ddbbca1"),"a1b224c3d2b2c1a11")
#     def test_count_alpha3(self):
#         self.assertNotEqual(alpha("aab1"),"ab11")


# if __name__ == '__main__' :
#     unittest.main()