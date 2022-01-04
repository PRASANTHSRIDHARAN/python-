import  calendar
month= int(input("enter the month "))
year = int(input("enter the year "))

calendar.setfirstweekday(calendar.SUNDAY)
mycal=calendar.month(year,month)
print(mycal)
