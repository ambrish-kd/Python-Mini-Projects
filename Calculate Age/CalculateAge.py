import time
from calendar import isleap

# returns the no of days in each month
def monthInDays(month, leapYear):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leapYear:
        return 29
    elif month == 2 and (not leapYear):
        return 28

# check for leap year
def leapYear(year):
    if isleap(year):
        return True
    else:
        return False

# Starting Point:-
name = input("\nInput your name: ")
age = input("\nInput your age: ")
localtime = time.localtime(time.time())

year = int(age)
month = year*12 + localtime.tm_mon
day = 0

begin_year = int(localtime.tm_year) - year
end_year = begin_year + year

for y in range(begin_year, end_year):
    if (leapYear(y)):
        day = day + 366
    else:
        day = day + 365

leap_year = leapYear(localtime.tm_year)

for m in range(1, localtime.tm_mon):
    day = day + monthInDays(m, leap_year)

day = day + localtime.tm_mday

print("\n%s's age is %d years or " % (name, year), end="")

print("%d months or %d days\n" % (month, day))
