# 19.Write a Python program to extract year, month, date and time using Lambda. I/p:
# 2020-01-15 09:03:32.744178

# O/p :
# Year : 2020
# Month : 1
# Day : 15
# Time : 09:03:32.744178


# import datetime

# # Define the datetime string
# datetime_str = '2020-01-15 09:03:32.744178'

# # Define the lambda function to extract year, month, date, and time
# extract = lambda dt: (dt.year, dt.month, dt.day, dt.time())


# # # Convert the datetime string to datetime object
# datetime_obj = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S.%f')
# print(datetime_obj)

# # # Extract year, month, date, and time using the lambda function
# year, month, day, time = extract(datetime_obj)

# # # Print the extracted values
# print('Year :', year)
# print('Month :', month)
# print('Day :', day)
# print('Time :', time)

datetime = '2020-01-15 09:03:32.744178'
get_date_and_time = lambda data: tuple(data.split())
date, time = get_date_and_time(datetime)
split_date = lambda date: date.split('-')
day, month, year = split_date(date)
print(day, month, year, time)
print('Year :', year)
print('Month :', month)
print('Day :', day)
print('Time :', time)

