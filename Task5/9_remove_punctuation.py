# 9. For the given sentence, return the average word length. 
# sentence = "I need to work very hard to learn more about algorithms in Python!" 
# Note: Remember to remove punctuation first.

def remove_punctuation(string):
    punctuation = ",.!():;/-?"
    string = string.translate(string.maketrans("","",punctuation))
    print(string)
    c = 0
    for i in range(len(string)):
        c += 1
        
    string = string.split(' ')
    print(string)

    return c//len(string)


sentence = "I need to work very hard. To learn more about algorithms in Python!"
print(remove_punctuation(sentence))
