# 7. Reverse the below string without changing the position of special characters . s = "adfw$vf&yvy*ugv%uy"

s = "adfw$vf&yvy*ugv%uy"
print(s)
l = list(s)
start = 0
end = len(l)-1

while start < end:
    if not l[start].isalnum():
        start += 1
    elif not l[end].isalnum():
        end -= 1
    else:
        l[start],l[end] = l[end],l[start]
        start += 1
        end += -1
print(''.join(l))


