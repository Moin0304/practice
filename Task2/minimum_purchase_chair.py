# 27. Need to find minimum number of new chair purchase for work area with simulated set of array
# values.
# C - A new employee comes to work area and new chair need to purchase
# R - Employee from work area goes to meeting room and free up the chair
# U - Employee comes from meeting room and occupy the chair
# L - Leaves the work area and free up the chair
# Input :
# n = 3
# simulated value : ['CCRLU', 'CRLCUC', 'CCCC']
# Output:
# 2
# 2
# 4

def minimum_number_chair_purchase(simulated_value):
    available_chairs = 0
    chairs_purchase = 0
    dictionary = {'C':1,'R':-1,'U':1,'L':-1}
    for sim in simulated_value:
        if dictionary[sim] == 1:
            if available_chairs > 0 :
                available_chairs -= 1
            else:
                chairs_purchase += 1
        else:
            available_chairs += 1

    return chairs_purchase
n = int(input("enter the number: "))
simulated_values = []
for i in range(n):
    simulated_values.append(input("enter the simulated_value: "))
for value in simulated_values:
    print(minimum_number_chair_purchase(value))
    

    