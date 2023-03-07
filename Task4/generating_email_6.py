
# 6.Define the logic for generating the email id based on username and department Get the username and department as a input and create a email id from it
# input :
# username : msys department: automation
# output:
# msys.automation@gmaiI.com
# Note : Generated email id should contain @ and should end with .com

def generate(user,depart):
    c = '@gmail.com'
    result = user+'.'+depart+c
    return result
user = input('enter the name: ')
depart = input('enter the department: ')
print(generate(user,depart))