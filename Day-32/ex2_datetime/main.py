import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(year)

date_of_birth = dt.datetime(year=1989, month=9, day=6, hour=7)
print(date_of_birth)