#Write a Python function that takes a list of integers and returns the sum of all the even numbers in the list.

def sum_of_even_numbers(list):
    sum = 0
    for i in range(len(list)):
        if list[i]%2 ==0:
            sum +=list[i]
    return sum

list = [ 10,2,4,1,5,7,8,4,]

print(sum_of_even_numbers(list))

#Write a function that takes two lists as input and returns a new list containing all the 
# elements that are common to both input lists.

def common(list,list1):
    l2 = []
    for i in list:
        for j in list1:
            if i == j:
                l2.append(j)
    return l2

list = [1,2,3,4,5]
list1 = [ 3,4,5,6,7]
print(common(list,list1))

#Write a program to find the largest number in a list of integers.

def largest(list):
    l = max(list)
    return l 
list = [23,45,17,82,90]
print(largest(list))

#Write a function that takes a list of strings and returns a new list with all the strings in the original list converted to uppercase.
# Write a function that takes a list of strings andreturns a new list with all the strings in the original list converted to uppercase.

def list_upper(list):
    list1 = []
    for i in list:
        a = i.upper()
        list1.append(a)
    return list1
list = ["moin","suhas","nandu","vishal"]
print(list_upper(list))

#Write a Python program that takes a list of integers and removes all the duplicates, returning a new list without duplicates.

def remove_duplicate(list1):
    new_list = []
    for i in range(len(list1)):
        duplicate = False
        for j in range(i+1,len(list1)):
            if list1[i] == list1[j]:
                duplicate = True
                break
        if not duplicate:
            new_list.append(list1[i])
    return new_list

list1 = [1, 2, 3, 2, 1, 4, 5, 3]
new_list = remove_duplicate(list1)
print(new_list)



# def remove_duplicates(my_list):
#     return list(set(my_list))

# my_list = [1, 2, 3, 2, 1, 4, 5, 3]
# new_list = remove_duplicates(my_list)
# print(new_list)

#   or 
# def remove_duplicates(list):
#     return list(dict.fromkeys(list))

# list = [1, 2, 3, 2, 1, 4, 5, 3]
# new_list = remove_duplicates(list)
# print(new_list)

#Write a function that takes a list of integers and returns the product of all the elements in the list.

def product(list):
    pro = 1
    for i in list:
        pro *= i
    return pro        
list = [ 1,2,3,4,5,6]
prod = product(list)
print(prod)

#Write a Python program that takes a list of integers and returns a new list with only the odd numbers from the original list.

def oddnumber(list):
    list1 = []
    for i in range(len(list)):
        if list[i] %2 != 0:
            list1.append(list[i])
    return list1
list = [1,2,3,4,5,6,7]
new_list = oddnumber(list)
print(new_list)

#Write a function that takes a list of strings and returns a new list with all the strings that have a length greater than or equal to 5.

def list_of_string(list):
    list1 = []
    for i in list:
        if len(i) >= 5:
            list1.append(i)
    return list1
list = ["moinali","suhasjc","meghanath","ramesh","afan","ajin"]
new_list = list_of_string(list)
print(new_list)

        



