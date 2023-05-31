# DAY - 33: Datetime module

import datetime as dt

now = dt.datetime.now()
print(now)
year = now.year
print(year)
day_of_week = now.weekday()
print(day_of_week)

# Creating a new datetime object with year, month and date
date_of_birth = dt.datetime(day=1, month=12, year=2005)  # hour,min,... have default values but d, m, y has to be given.
print(date_of_birth)

