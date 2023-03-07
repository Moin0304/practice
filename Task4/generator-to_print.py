# 19.Define a generator to print the numbers between o to n (including) which are divisible by 5 and
#  should be even
# N = 20
# Output : 10 20

def number_divisible_by_5_even(n):
    nums = (i for i in range(1,n+1) if i%2==0 and i%5==0)
    return nums


num = number_divisible_by_5_even(20)
for i in num:
    print(i,end=' ')