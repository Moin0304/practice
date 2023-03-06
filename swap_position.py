def swap_position(list,pos1,pos2):
    list[pos1],list[pos2] = list[pos2],list[pos1]
    return list
list = [1,2,3,4,5,6,7,8]
print(swap_position(list,2,5))