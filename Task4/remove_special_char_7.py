# 7 In the given string, remove the special characters and add a space instead of that
#  “Msys&Technologies@Chennai*

def remove_special_char(string):
    special = ['!','@','#','$','%','^','&','*']
    result = ""
    for i in range(len(string)):
        if string[i] in special:
            r = string[i].replace(string[i],' ')
            result += r
        else:
            result += string[i]
    return result

str = "Msys&Technologies@Chennai*"
print(remove_special_char(str))