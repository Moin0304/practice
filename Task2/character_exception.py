# 19. Write a function which takes input string from the user as argument and the character also taken
# by the user as the argument and remove all the occurences of that character from the string. Also if
# the given character is not present in the string your function should raise the exception stating that
# “Given character is not present in the string. Please try with a new one”.


def remove_char_in_sentance(sentance,char):
  
    if char not in sentance:
        raise Exception("given character is not in sentance")
    else:
        return sentance.replace(char, '')

sentance = input("enter a sentance: ")
char = input("enter a character: ")

try:
    result = remove_char_in_sentance(sentance,char)
    print(result)
except Exception as error:
    print(error)

