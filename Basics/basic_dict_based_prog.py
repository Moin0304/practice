#Write a program that takes a list of numbers and returns a dictionary containing the count of even numbers
#  and the count of odd numbers in the list.

def odd_n_even(list):
    count_even = 0 
    count_odd = 0
    for i in list:
        if i%2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return {"even":count_even,"odd":count_odd}

list = [3, 4, 6, 7, 9, 12, 15]
print(odd_n_even(list))

#Write a program that takes a list of integers as input and returns a dictionary 
# containing the count of each unique integer in the list.

def count(list):
    dict = {}
    for i in list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
list = [1, 2, 3, 1, 2, 4, 5, 3, 2]
print(count(list))

#Write a program that takes a list of words as input and 
# returns a dictionary containing the length of each word in the list.

def list_of_words(list):
    count = {}
    for i in list:
        count[i] = len(i)
    return count

list = ["moin","suhas","nandu","vishala"]
print(list_of_words(list))

#Write a program that takes a string as input and
#  returns a dictionary containing the count of each word in the string.

def count_words(list):
    words = list.split()
    count = {}
    for i in words:
        if i in count:
            count[i] += 1
        else:
            count[i] =1
    return count
list = "the quick brown fox jumped over the lazy dog"
print(count_words(list))

#Write a program that takes two lists of equal length, one containing keys and the other containing values, and
#  returns a dictionary mapping each key to its corresponding value

def mapping(list1,list2):
    dict = {}
    for i in range(len(list1)):
        dict[list1[i]] =list2[i]
    return dict
list1 = [1,2,3,4,5]
list2 = ["moin","suhas","nandu","vishala","meghu"]
print(mapping(list1,list2))

#Write a program that takes a list of dictionaries as input and 
# returns a dictionary containing the total count of each key across all dictionaries.

def count_keys(dicts):
    result_dict = {}
    for d in dicts:
        for key in d:
            if key in result_dict:
                result_dict[key] += 1
            else:
                result_dict[key] = 1
    return result_dict

# example usage
dicts = [
    {"a": 1, "b": 2, "c": 3},
    {"a": 2, "b": 3},
    {"a": 3, "b": 3, "c": 3, "d": 4}
]
result = count_keys(dicts)
print(result)  # {"a": 6, "b": 8, "c": 6, "d": 1}
