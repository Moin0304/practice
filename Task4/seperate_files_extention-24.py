# 24.Define a logic for identifying the different files (In different format:.csv, .txt)
#  which are part of a directory
# Input : You can create a directory and create the files with two different formats (Manually for the input)
# Output : Create two different directories and store this files separately based on the extension
# Example :
# Input:
# Assume file1.csv, file2.txt, file3.csv, file4.txt are present inside a directory (Any name)
# Output:

# CSV - [Directory with the name CSV] file1.csv

# file3.csv
# TXT - [Directory with the name TXT] file4.txt
# fiIe2.txt


import os
import shutil

dir_path = "D:\\practice\\practice\\Task4\\files"
files = os.listdir(dir_path)

for file in files:
    extension = file.split(".")[-1]
    if not os.path.exists(os.path.join(dir_path, extension.upper())):
        os.mkdir(os.path.join(dir_path, extension.upper()))
        
    shutil.move(os.path.join(dir_path, file), os.path.join(dir_path, extension.upper(), file))
