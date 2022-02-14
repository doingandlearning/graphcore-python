# Ask the user for a day, month, and year.
day   = int(input("Enter a day (1-31): "))
month = int(input("Enter a month (1-12): "))
year  = int(input("Enter a year (0 to 2099): "))

# Add the rest of your code here.
isLeapYear = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

if month == 2:
    if isLeapYear:
        days_in_month = 29
    else:
        days_in_month = 28
elif month in (9, 4, 6, 11):
    days_in_month = 30
else:
    days_in_month = 31

isValidYear = year >= 0 and year <= 2099
isValidDaysInMonth = day >= 1 and day <= days_in_month
isValidMonth = month >= 1 and month <= 12

isValid = isValidYear and isValidDaysInMonth and isValidMonth

if isValid:
    for day in range(1, days_in_month + 1):
        print(f"{day:02d}/{month}/{year}")
