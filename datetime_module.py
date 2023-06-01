# DAY - 33: Datetime module
from datetime import datetime, timedelta

now = datetime.now()
print(now)
year = now.year
print(year)
day_of_week = now.weekday()
print(day_of_week)

# Creating a new datetime object with year, month and date
date_of_birth = datetime(day=1, month=12, year=2005)  # hour,min,... have default values but d, m, y has to be given.
print(date_of_birth)


today = datetime.now().date()
yesterday = str(today - timedelta(days=1))  # Getting yesterday as a datetime object
day_before_yesterday = str(today - timedelta(days=2))
print(today, yesterday)
