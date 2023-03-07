# 5.Let’s consider there is a list which contains usernames, You have received requirement to add one more username to the list (without using append and assignment approaches)

# input : [“user1”,”user2”]
# output : [“user1”,”user2”,”user3”]

# 1st Approach

def add_element(list):
    list[len(list):] = ["user3"]
    return list
list = ['user1','user2']
print(add_element(list))


# 2nd Approach

old_list = ["user1", "user2"]
new_username = "user3"
new_list = [*old_list, new_username]  # splat operator , it is used to unpack the elements
print(new_list)
