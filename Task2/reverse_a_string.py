# 16. Write a function which will take a string argument and reverse the words in the string. For
# example – Input string -- “Hello World”. Output should be “olleH dlroW”.

word = "Hello World"
list_words = word.split()
print(list_words)
l = []
for i in range(len(list_words)):
    l.append(list_words[i][::-1])
l4 = " ".join(l)

print(l4)