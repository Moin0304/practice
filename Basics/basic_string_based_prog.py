# Write a Python program that takes a string and prints its length.

s = "string"
print(len(s))

#Write a Python program that takes a string and counts the number of vowels in it.

vowels = ["a","e","i","o","u"]
count = 0
for i in s:
    if i in vowels:
        count += 1
print(count)

#Write a Python program that takes a string and reverses it.

s1 = s[::-1]
print(s1)

s2 = ""
for i in range(len(s)-1,-1,-1):
    s2 += s[i]
print(s2)

#Write a Python program that takes a string and checks if it is a palindrome.

s1 = "moM"
s1 = s1.lower()
s2 = s1[::-1]
if s1 == s2:
    print("its a polindrome")
else:
    print("its not a polindrome")

#Write a Python program that takes two strings and checks if they are anagrams of each other.

def anagrams(s1,s2):
    if sorted(s1) == sorted(s2):
        return "its a anagram"
    else:
        return "its not a anagram"
s1 = input("enter a 1st string")
s2 = input("enter a 2nd string")
print(anagrams(s1,s2))

#Write a Python program that takes a string and converts it to lowercase.

def string(s):
    s = s.lower()
    return s
s = "MOIN ALI KHAN"
print(string(s))

#Write a Python program that takes a string and removes all the vowels from it.

def remove_vowels(s):
    vowels = ["a","e","i","o","u"]
    s1 = ""
    for i in s:
        if i not in vowels:
            s1 += i
    return s1
s = "Moin Ali Khan"
print(remove_vowels(s))

#Write a Python program that takes a string and removes all the consonants from it.

def remove_vowels(s):
    vowels = ["a","e","i","o","u"]
    s1 = ""
    for i in s:
        if i.lower() not in vowels and i.isalpha():
            s1 += i
    return s1
s = "Moin Ali Khan"
print(remove_vowels(s))

#Write a Python program that takes a string and checks if it contains only digits.

def contains_digits(s):
    for i in s:
        if not i.isdigit():
            return False
    return True
s = "12345s"
print(contains_digits(s))

#Write a Python program that takes a string and removes all the spaces from it.

def remove_space(s):
   return s.replace(" ", "")
s = "Moin Ali Khan"
print(remove_space(s))
        


