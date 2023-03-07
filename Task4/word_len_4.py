# 4.Define a function which returns dictionary that stores the words and it’s length from the given text
# text = “Be happy”
# Expected Output : {“Be'.2,”happy”:5}

def word_len(str):
    s = str.split(' ')
    result = {}
    for i in s:
        if i not in result:
            result[i] = len(i)
    return result
str = "Be happy"
print(word_len(str))
