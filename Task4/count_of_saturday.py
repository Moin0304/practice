# 17. Define the function which returns the counts of saturdays part of a year (year is an input [Ex: 2022])

import datetime

def count_of_saturday(year):
    start = datetime.date(year,1,1)
    end = datetime.date(year,12,31)
    nums_days = (end - start).days + 1
    num_saturdays = sum(1 for i in range(nums_days) if (start + datetime.timedelta(i)).weekday() == 5)
    

    return num_saturdays

print(count_of_saturday(1997))