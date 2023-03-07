# 28.Standardize mobile numbers when given N mobile numbers. Sort them in ascending order.
#  Print them in the standard format.

def phone_number(list):
    n = list.sort()
    list_sorted_number = []
    for i in range(len(list)):
        list_sorted_number.append("+91 "+ list[i])
    return list_sorted_number
list = ['9591284895','7848996868','8050456321']
print(phone_number(list))

