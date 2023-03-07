# 30.Convert each list element to a key-value pair. ex:
# Input : test_list = [2323, 82, 129388, 95]
# Output : {23: 23, 8: 2, 129: 388, 9: 5}



def list_to_key_value(list):
    d = {}
    for i in list:
        d.update({int(str(i)[:len(str(i))//2]):int(str(i)[len(str(i))//2:])})
    return d
list = [2323, 82, 129388, 95]
print(list_to_key_value(list))