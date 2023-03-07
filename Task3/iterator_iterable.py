l = [1,2,3]
print(dir(type(l)))
print()
a=iter(l)
print(a)
print(dir(type(a)))
for i in a:
    print(i)

print(next(a))
print(next(a))
print(next(a))
for i in a:
    print(i)