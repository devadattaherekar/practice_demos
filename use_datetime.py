import datetime

print(datetime.datetime.now())
print(datetime.datetime.today())

todays_date=datetime.date(2024,6,19)
print(todays_date)
print(todays_date.day,todays_date.month,todays_date.year)

todays_time=datetime.time(18,30,15)
print(todays_time)
print(todays_time.hour,todays_time.minute,todays_time.second)

dt1=datetime.date(2025,6,12)
dt2=datetime.timedelta(45)
print("Date after 45 days from today",dt1+dt2)

dt2=datetime.date(2026,2,12)
print("Difference between dates",dt2-dt1)

actual_date=dt1=datetime.date(2025,6,12)
print(actual_date)
format_custom_date=datetime.datetime.strftime(dt1,"Month %B , Weekday %A %d/%m/%Y")
print(format_custom_date)

try:
    custom_date = input("Enter date in dd-mm-YYYY format")
    mydate=datetime.datetime.strptime(custom_date,"%d-%m-%Y")
except Exception as errmsg:
    print(errmsg)
else:
    print(datetime.datetime.strftime(mydate, "Month %B , Weekday %A %d/%m/%Y"))