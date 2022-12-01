import calendar
import datetime
a = [int(x) for x in input().split()]
d = a[0]
m = a[1]
def findDay(date): 
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
    return (calendar.day_name[born]) 
date = "{} {} 2009".format(d, m)
print(findDay(date))