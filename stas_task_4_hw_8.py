import datetime

now = datetime.datetime.now()

year = lambda t: datetime.datetime.timetuple(t)[0]
month = lambda t: datetime.datetime.timetuple(t)[1]
day = lambda t: datetime.datetime.timetuple(t)[2]

print(year(now))
print(month(now))
print(day(now))
