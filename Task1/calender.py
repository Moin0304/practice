#Write a function where month and year are taken as arguments 
# which returns the output with all the dates of saturdays occuring the month

# 1st Approch

import calendar

def list_of_saturday(month,year):
    num_days = calendar.monthrange(year, month)[1]
    saturday = []
    for day in range(1,num_days+1):
        weekday = calendar.weekday(year, month, day)

        if weekday == 5:
            saturday.append(day)
    return saturday

list = list_of_saturday(1,2023)
# print(list)


# 2nd Approch

def is_leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False

def list_of_saturdays(month,year):
    
    Month_code = {1:(1,31),2:(4,28),3:(4,31),4:(0,30),5:(2,31),6:(5,30),7:(0,31),8:(3,31),9:(6,30),10:(1,31),11:(4,30),12:(6,31)}
    century_code ={15:0,16:6,17:4,18:2,19:0,20:6,21:4,22:2,23:0}
    day_code = {0:"sat",1:"sun",2:"mon",3:"tue",4:"wed",5:"thu",6:"fri"}

    mc = Month_code[month][0]
    cc = century_code[year//100]
    number_of_years_completed  = year % 100
    number_of_leap_year = number_of_years_completed // 4

    number_of_days_in_month = Month_code[month][1]

    leap_year = is_leap_year(year)
    if leap_year == True and month == 2:
        number_of_days_in_month += 1
    
    diff = 0

    if leap_year ==True and month in (1,2):
        diff = 1


    result = []
    for day in range(1,number_of_days_in_month+1):
        total = day + mc + cc + number_of_years_completed + number_of_leap_year - diff
        days = total % 7
        if day_code[days] == "sat":
            result.append(day)
    return result




month = int(input("enter the month: "))
year = int(input("enter the year: "))
list = list_of_saturdays(month,year)
print(list)
