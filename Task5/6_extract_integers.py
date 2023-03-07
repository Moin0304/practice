# 6. Read a given file and extract the integers from each line, 
# concatenate all the integers present in the same line and print the sum of all these integers. 
# eg: <File content>
#  He is 32 yrs old and his son is 7 yrs old .
#  She is 27 yrs old and her daughter is 2 yrs old .


def extract_integers(f):
    with open(f,"r") as file:
        line = file.readlines()
    num = 0
    for i in line:
        s = ''
        for j  in range(len(i)):
            if i[j].isdigit():
                s += i[j]
        num += int(s)
    return num
print(extract_integers("6_extract_integers.txt"))


