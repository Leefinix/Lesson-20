from datetime import date, time, datetime

today = date.today()
now = datetime.now()

print("Today's date is", today)
print("\nThe Current Date and Time is", now)
print("\nDate Components: ", today.year, today.month, today.day)