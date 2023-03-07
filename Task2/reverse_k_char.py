# 28. Given a string s and an integer k, reverse the first k characters for every 2k characters counting
# from the start of the string.
# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater
# than or equal to k characters, then reverse the first k characters and leave the other as original.
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Input: s = "abcd", k = 2
# Output: "bacd"



def reverse_string(s, k):
    s = list(s)
    n = len(s)
    for i in range(0, n, 2*k):
        start = i
        end = min(i+k-1, n-1)
        
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
    
    return ''.join(s)

s = input("enter the string: ")
k = int(input("enter to reverse: "))
result = reverse_string(s,k)
print(result)