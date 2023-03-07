# 9.Given a string “abcde”, Display the output as “a1b2c3d4e5”



def aplphabet_index(string):
    result = ''
    for i in range(0,len(string)):
        result += string[i]+str(i+1)
    return result
alpha = 'abcde'
print(aplphabet_index(alpha))