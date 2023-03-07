#22. Write a function where month and year are taken as arguments which returns the output with all the dates of saturdays occuring the month.

import calendar

def get_saturdays_in_month(month, year):
    # Get the number of days in the month
    num_days = calendar.monthrange(year, month)[1]
    
    # Initialize an empty list to store the Saturdays
    saturdays = []
    
    # Loop through all the days in the month
    for day in range(1, num_days + 1):
        # Use the calendar module to get the day of the week (0 = Monday, 6 = Sunday)
        weekday = calendar.weekday(year, month, day)
        
        # If the day is a Saturday (5 = Saturday), add it to the list
        if weekday == 5:
            saturdays.append(day)
    
    return saturdays

saturdays_in_january_2022 = get_saturdays_in_month(1, 2022)
print(saturdays_in_january_2022)
# Output: [1, 8, 15, 22, 29]
