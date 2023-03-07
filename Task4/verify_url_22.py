# 22.Define the logic for verifying whether URL is Valid or Invalid Requirements for Valid URL
# •Should not contain any Special characters [,*,&,%,$,#,@,!] and Spaces
# •Should start with https://
# Input : URLs will be stored inside a file , read the URLs from the input file [input.txt]
# Output : Generate a .txt file which contains the information whether URL is valid or not 
# ( URL, Status [valid/invalid])
# Example:
# Input
# Input.txt [text file]
# https://m http s://m
# Output:
# 1.https://m, valid
# 2.http s://m, invalid

# Note: Define the logic with different approaches [1. Using RegEx 2. Without RegEx]

def read_url(file_name):
    with open(file_name,'r') as input_file:
        return input_file.readlines()
urls = read_url('valid_url_22.txt')
print(urls)

def valid_url(urls):
    with open("output.txt",'w') as output_file:
        special = "!@#$%^&*()\"\\'{}[]><,?_-+=|"
        
        for url in urls:
            result = True
            url = url.rstrip("\n")
            if url.startswith("https://"):
                for i in special:
                    if i in url:
                        result = False
                        break
            else:
                result = False
            
            if result:
                output_file.write(f"{url},valid\n")
            else:
                output_file.write(f"{url},invalid\n")

valid_url(urls)

                        



