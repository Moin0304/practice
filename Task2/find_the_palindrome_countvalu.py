# 22. Find the palindrome words with the count value from the given string.Output should be in
# form of dict. key will be palidrome word and value will be number of occurence.

# i/p given a string - Nittin & his mom went to a park last friday. His Mom observed that the weather
# was too cool. Nittin also met his sis. If we reverse the number 1331 then we also get 1331.
# o/p - {'nittin': 2, 'mom': 2, 'sis': 1, '1331': 2}



def is_palindrome(i):
    if i == i[::-1]:
        return True
    return False

def polindrom_count(string):
    lower_case = string.lower()
    string = lower_case.replace("."," ")
    new_list = string.split()
    # print(new_list)
    count = {}
    for i in new_list:
        if is_palindrome(i) and len(i)>1:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
    return count
    
string = 'Nittin & his mom went to a park last friday. His Mom observed that the weather was too cool. Nittin also met his sis. If we reverse the number 1331 then we also get 1331.'
print(polindrom_count(string))

        







