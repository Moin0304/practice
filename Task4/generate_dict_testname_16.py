# result = {}
# with open('file1_16.txt') as file:
#     for status in file:
#         status = status.strip('\n')
#         k,v = status.split('-')
#         print(k,v)
#         result[k] = v
# print(result)


# Open the two input files and read in their contents
with open("file1_16_.txt", "r") as file1, open("file1_16.txt", "r") as file2:
    testnames = file1.read().split('\n')  # Read testnames from File1.txt
    teststatuses = file2.read().split('\n')  # Read test statuses from File2.txt
print(testnames)
# Generate a dictionary with testname as key and status as value
test_dict = {}
for i in range(len(testnames)):
    testname = testnames[i]
    status = teststatuses[i].split("-")[1]  # Extract the status from the "testname-status" string in File2.txt
    test_dict[testname] = status

# Print the resulting dictionary
print(test_dict)
