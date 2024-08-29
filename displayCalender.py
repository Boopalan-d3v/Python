import calendar
year = int(input('Enter the Year :'))
month = int(input('Enter the Month :'))
cal = calendar.month(year, month) # 1st Year and 2nd Month this should not be changed
print(cal)