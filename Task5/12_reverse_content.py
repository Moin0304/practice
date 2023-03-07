# 12. Write a Python Program to Reverse the Content of a File.
#  Input :- I am
#           new to this
#           world of 
#           Python. 
# Output :- Python.
#           world of
#           new to this 
#           I am

def reverse_content(f):
    with open(f,'r') as input_file:
        l = []
        data = input_file.readlines()
        
        with open('12_output','w') as output_file:
            data = data[::-1]
            output_file.writelines(data)
            
print(reverse_content('12_reverse_content.txt'))

