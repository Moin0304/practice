# 17. Write a program to replace duplicate adjacent alphabets from given string with ‘_’.
# For Example -- input given string : 'abcdaa hssbbye' and output : ‘abcda_ hs_b_ye’


String_1 = input("enter a string: ")
res = []
str = ""
for i in String_1:
    if i == str:
        res.append("_")
    else:
        res.append(i)
        str = i
    new_string = "".join(res)

print(new_string)




