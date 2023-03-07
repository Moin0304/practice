# 25.Write a function that employs regular expressions to ensure the password given to the function is strong.
#  A strong password is defined as follows:
# -at least eight characters long
# -contains one uppercase character
# -contains one lowercase character
# -has at least one digit
# -has at least one special character

import re

def valid_password(p):

    if len(p) < 8:
        return False

    if not re.search('[A-Z]',p):
        return False
    if not re.search('[a-z]',p):
        return False
    if not re.search('[0-9]',p):
        return False
    if not re.search('[^A-Za-z0-9]',p):
        return False
    return True
    
password = input('enter a password: ')
print(valid_password(password))