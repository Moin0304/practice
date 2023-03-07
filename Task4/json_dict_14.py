# 14.Define a function which can read json file and displays the data present in it to the console 
# in dictionary format
# Note : Please create .json file and store the sample data in it and read the json file,
#  display the data in dictionary format

import json


def read_json(file_name):
    with open(file_name,'r') as file:
        x = file.read()
        y = json.loads(x)
        return y

data = read_json('dic.json')
print(data['age'])
for i in data.items():
    print(i)

    