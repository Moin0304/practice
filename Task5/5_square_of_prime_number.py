# 5.From given list of numbers, create a list of square of prime numbers .
#  l1 = [1, 4, 6, 11,15, 24, 19, 25, 27, 30,17]


def is_prime(num):
    if num < 2 :
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def prime_square(list):
    prime_square_list = []
    for num in list:
        if is_prime(num):
            prime_square_list.append(num**2)
    return prime_square_list

l1 = [1,2, 4, 6, 11,15, 24, 19, 25, 27, 30,17]
print(prime_square(l1))
