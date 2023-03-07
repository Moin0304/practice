# 9.Create a function is_leap_year that accepts a year 
# and returns True if (and only if) the given year is a leap year.

def leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False

print(leap_year(int(input("enter a year: "))))
