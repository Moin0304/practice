dict = {3:"a",2:"c",1:"b"}
sorted_dict = {key: dict[key] for key in sorted(dict)}
for key in sorted_dict:
    print(key, sorted_dict[key])

l = sorted(dict.items())
d = {k:v for k,v in l}
print(d)