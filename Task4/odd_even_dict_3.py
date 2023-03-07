# 3 Define logic for identifying the even numbers and odd numbers from the given list and generate a dictionary as follows
# numbers = [4,5,7,2,9,8]
# result	= (“even”:[4,2,8],”odd'.[5,7,9]}

def odd_even_dict(number):
    result = {}
    
    for i in number:
        if i%2 == 0:
            if 'even' in result:
                result['even'] += [i]
            else:
                result['even'] = [i]
        else:
            if 'odd' in result:
                result['odd'] += [i]
            else:
                result['odd'] = [i]
    
    return result
numbers = [4,5,7,2,9,8]
print(odd_even_dict(numbers))