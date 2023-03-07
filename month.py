import calendar

def saturday(month,year):
    num_days = calendar.monthrange(year, month)[1]
    saturdays = []
    for day in range(1,num_days+1):
        weekday = calendar.weekday(year, month, day)

        if weekday == 5:
            saturdays.append(day)
    return saturdays

s = saturday(1,2022)
print(s)
