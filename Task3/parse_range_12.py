
# 12.Write a function called parse_ranges, which accepts a string containing ranges of numbers and
#  returns an iterable of those numbers.
# Ex: >>> parse_ranges('1-2,4-4,8-13')
#  [1, 2, 4, 8, 9, 10, 11, 12, 13]

def parse_range(string):
    s = string.split(',')
    print(s)
    result = []
    for i in s:
        bound = i.split('-')
        # print(bound)
        start = int(bound[0])
        end = int(bound[-1])+1
        result += list(range(start,end))
    return result

parse = parse_range('1-2,4-4,8-13')
print(parse)
