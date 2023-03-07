# 6.Write a function to_percent which accepts a number representing a ratio and  returns a 
# string representing the percentage representation of the number to one decimal place.



# def to_present(ratio):
#     return  f"{ratio * 100 : .1f}"

# def to_present(ratio):
#     percent = ratio * 100
#     return  "{0:.1f}%".format(percent)


# print(to_present(200/300))

import re

def ratio(num):
    try:
        if ':' in num:
            x = re.split(':',num)
        else:
            x = re.split('/',num)
        num = int(x[0])/int(x[1])
        dec_num = num *100
        return round(dec_num,1)
    except:
        return "enter valid ratio for example: 1:2 or 1/2"
number = input('enter a ratio number to convert into percentagae: ')
print(ratio(number))
