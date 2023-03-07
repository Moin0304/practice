# 24. You have given a string str1 = "abcbaefabcabchijkl"
# your task is to find the combination of given word without repetition, present in the string , given
# word 'abc'
# o/p = 7
# explaination :
# abc, cba,
# cba,
# bca, acb
# cab, bac

str1 = "abcbaefabcabchijkl"
word = 'abc'
combination = "abc,bca,cab,cba,acb,bac"



feet = int(input('enter the height: '))
bounce_count = 0
while feet > 0:
    feet = feet//2
    bounce_count += 1
print(bounce_count)