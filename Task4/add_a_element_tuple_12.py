# 12.Solve the following scenarios
# •Let’s assume that there is a tuple containing username, You have got a requirement to add password 
# also into it.
# oInput : (“user1”)
# oOutput : (“user1”,”password1”)
# •Below logic is failing with an error message, Instead of auto generated Error, 
# Please display the user defined message saying “Error : Cannot concatenate String and Number”
# print(“msys” + 2007)

tuple = ('user1',)
tuple1 = tuple + ('password1',)
print(tuple1)

print()

try:
    b = 'msys' + 2007
except:
    print('you cannot concatenate string with int')
