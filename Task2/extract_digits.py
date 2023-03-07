# 20. You are given a string having alphabets,digits,special characters. Write three different functions
# to extract the digits[should be in sorted order], special character & vowels[should be in reverse]
# from the given string.
# i/p string : "abcd123bye09@8"
# o/p: digits - 012389
# special character - @
# vowels - ea



def is_digits(string):
    digit = ''
    for i in string:
        if i.isdigit():
            digit += i
    sort = sorted(digit)
    digits = "".join(sort)
    return digits

def is_vowel(string):
    vowels = 'aeiouAEIOU'
    vowel = ''
    for i in string:
        if i in vowels:
            vowel += i
    return vowel[::-1]

def is_special_character(string):
    special = "!@#$%^&*"
    special_char = ''
    for i in string:
        if i in special:
            special_char += i
    return special_char

string = input("enter a string: ")

print(is_digits(string))
print(is_vowel(string))
print(is_special_character(string))


