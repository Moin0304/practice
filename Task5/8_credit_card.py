# 8. Write a function in Python that accepts a credit card number. It should return a string 
# where all the characters are hidden with an asterisk except the last four.
# For eg., if the credit card no. is “4509876278910046”, then function should return “************0046”.

def hidden(str):
    asterisk = len(str)-4
    if len(str) == 16:
        # for i in range(asterisk):
        #     print("*",end='')
        char_encrypted = asterisk*'*'
        char_displayed = str[asterisk:]
        show = char_encrypted + char_displayed
    return show

string = "1234567898765432"
print(hidden(string))