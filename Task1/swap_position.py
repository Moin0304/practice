#Write a function swap_element that contains two args which will be the position of elements present in the list. The function must swap the elements present in those positions.
#Input: [1,2,3,4,5,6,7,8] function: swap_element(arg1, arg2)


# 1st Approch

def swap_elements(list,pos):
    pos1 , pos2 = pos
    try :
        if pos1 != pos2:
            list[pos1],list[pos2] = list[pos2],list[pos1]
            return list
    except IndexError:
        print("error : enter the value within the range ")

list = list(int(i) for i in input("Give a list: ").split())
pos1 = int(input("enter the 1st position: "))
pos2 = int(input("enter the 2nd position: "))
print(swap_elements(list,(pos1,pos2)))


#2nd Approch

def swap_position(list,pos1,pos2):
    list[pos1],list[pos2] = list[pos2],list[pos1]
    return list
list = [1,2,3,4,5,6,7,8]
print(swap_position(list,2,5))