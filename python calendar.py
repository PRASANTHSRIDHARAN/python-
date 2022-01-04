import  calendar
month= int(input("enter the month \n"))
year = int(input("enter the year \n"))

calendar.setfirstweekday(calendar.SUNDAY)
mycal=calendar.month(year,month)
print(mycal)