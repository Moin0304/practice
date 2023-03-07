
# 20.Create a function that determines which day of the month the San Diego Python meetup should be.
# It should accept year and month arguments and should return a datetime.date object representing 
# the day of the month for the meetup.
# >>> meetup_date(2012, 3)
# datetime.date(2012, 3, 22)


import datetime

def meetup_date(year, month):
    # San Diego Python meetup is held on the fourth Thursday of every month
    first_day = datetime.date(year, month, 1)
    days_to_thursday = (3 - first_day.weekday() + 7) % 7
    meetup_day = first_day + datetime.timedelta(days=days_to_thursday, weeks=3)
    return meetup_day

print(meetup_date(2023,6))


    
