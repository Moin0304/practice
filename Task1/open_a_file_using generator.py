#How do you open a file of large size, say around 10GB? So that program should not crash

# 1st Approch

# import os

# file = "big_data.txt"
# text = open(file)
# print(f"\nfile size in bytes  {os.stat(file).st_size}\n")
# print(f"file size in MegaBytes  {os.stat(file).st_size/(1024*1024*1024)}\n")
# # print(text)
# count = 0
# def generate_lines(lines):
#     for line in lines:
#         yield line

# print()

# generated_lines = generate_lines(text)

# print(next(generated_lines).replace("\n",""))
# print(next(generated_lines).replace("\n",""))
# print(next(generated_lines).replace("\n",""))

# for line in generated_lines:
#     count += 1
#     line = line.replace("\n","")
#     print(line)
# print(f"\nthe number of line in a file is:  {count}")
# text.close()


# 2nd Approch

import os
import time

def read_a_file(big_data):
    with open (big_data,"r") as file:
        while True:
            data = file.read(1000)
            if not data:
                break
            yield data
file_size_bytes = os.path.getsize("big_data.txt")
print(file_size_bytes)

for piece_of_byte in read_a_file("big_data.txt"):
    time.sleep(1)
    print(piece_of_byte)

