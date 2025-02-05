"""
return the day of tomorrow for the input date.
__author__ = Gvanderveen
__version__ = 0.1
"""

day = int(input("Enter the day : "))
month = int(input("Enter the month (number) : "))
year = int(input("Enter the year : "))

if month in (1, 3, 5, 6, 7, 10, 12):
    if day > 31:
        raise ValueError("invalid day")  # or print()
    day = (day % 31) + 1
elif month in (4, 8, 9, 11):
    if day > 30:
        raise ValueError("invalid day")
    day = (day % 30) + 1
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        if day > 29:
            raise ValueError("invalid day")
        day = (day % 29) + 1
    else:
        if day > 28:
            raise ValueError("invalid day")
        day = (day % 28) + 1
else:
    raise ValueError("invalid month")
if day == 1:
    month = (month % 12) + 1
if month == 1 and day == 1:
    year += 1

print(f"{day}/{month}/{year}")
