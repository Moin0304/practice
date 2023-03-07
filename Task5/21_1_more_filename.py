# 21.Write a program that takes one or more filenames as arguments and prints all the lines
#  which are longer than 40 characters. 
# Note :Use generator to solve this question.

# 1st Approach

def generate_lines(*args):
    for i in args:
        with open(i,'r') as file:
            for j in file.readlines():
                if len(j.rstrip()) > 40:
                    yield j.rstrip()

generated = generate_lines("12_output",'6_extract_integers.txt','12_reverse_content.txt')
for line in generated:
    print(line)


# 2nd Approach

def file(file1,file2):
    with open(file1,'r') as fp , open(file2,'r') as fp1:
        filedata = [line for line in fp.readline().splitlines()]
        filedata.extend([lines for lines in fp1.readline().splitlines()])
        # for i in filedata:
        #     if len(i) > 40:
        #         yield i
        gen1 = (line for line in filedata if len(line) > 40 )
    return gen1


gen = file("12_output",'18_pickle.txt')
for i in gen:
    print(i)

