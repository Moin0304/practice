#Write a python function with name reverse_vowel that takes one string as an argument and
#reverse the order of vowels present in the string. The function should return the string having
#reversed order of vowels. For example – If the input string which is given as argument is ‘Hello’
#then the output string should be ‘Holle’. You need to reverse the vowel irrespective of lowercase or
#uppercase.

# def is_vowel(c):
#     if (c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U'):
#         return True
#     return False

# def reverse_vowel(string):
#     j = 0
#     vowel = [0] * len(string)
#     string = list(string)
#     for i in range(len(string)):
#         if is_vowel(string[i]):
#             vowel[j] = string[i]
#             j += 1

#     for i in range(len(string)):
#         if is_vowel(string[i]):
#             j -= 1
#             string[i] = vowel[j]
 
#     return ''.join(string)

# string = "hello world"
# print(reverse_vowel(string))
        

def is_vowel(c):
    if (c=='a' or c=='e' or c== 'i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U'):
        return True
    return False

def swap_vowels(string):
    j = 0
    string = list(string)
    vowel = [0] * len(string)
    for i in range(len(string)):
        if is_vowel(string[i]):
            vowel[j] = string[i]
            j += 1
    
    for i in range(len(string)):
        if is_vowel(string[i]):
            j -= 1
            string[i] = vowel[j]
            

    return "".join(string)

string = input("enter a word: ")
print(swap_vowels(string))