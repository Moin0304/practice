# 15.Define logic for generating the random password with the provided length as an input

import random
def random_password(n):
    numbers = '1234567890'
    special = '!@#$%^&*()+:~`><?{}[]|\\=.-,_";\''
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = lower_case.upper()
    password = ''
    for i in range(n):
        password += random.choice(numbers + special + lower_case + upper_case)
    return password
n = int(input('enter the length: '))
print(random_password(n))