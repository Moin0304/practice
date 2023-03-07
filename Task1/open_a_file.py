import os

file = "big_data.txt"
text = open(file)
print(f"\nfile size in bytes  {os.stat(file).st_size}\n")
print(f"file size in MegaBytes  {os.stat(file).st_size/(1024*1024)}\n")
# print(text)
count = 0
for line in text:
    count += 1
    line = line.replace("\n","")
    print(line)
print(f"\nthe number of line in a file is:  {count}")
text.close()
