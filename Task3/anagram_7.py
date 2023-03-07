# 7.Write a function that accepts two strings and returns True if the two strings are anagrams of each other.

def anagram(string1,string2):
    if sorted(string1) == sorted(string2):
        return True
    else:
        return False

string1 = input("enter 1st string: ")
string2 = input("enter 2nd string: ")     
print(anagram(string1,string2))