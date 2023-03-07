# 18. dct = {111: "Eric", 112: "Kyle", 113: "Butters"}
# Load the above dictionary variable in a file 'test.txt' .
#  Now create a new dictionary variable (eg. dct2) and load the contents of the file 'test.txt' in it. 
#  Print the value of key '112' using the new dictionary variable .

# Note : Use pickling for solving this question. O/p : Kyle

import pickle

dct = {111: "Eric", 112: "Kyle", 113: "Butters"}

with open('18_pickle.txt','wb') as f:
    pickle.dump(dct,f)

with open('18_pickle.txt','rb') as f:
    dct2 = pickle.load(f)
print(dct2[112])
