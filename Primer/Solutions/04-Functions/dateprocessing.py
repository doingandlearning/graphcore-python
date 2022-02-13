def isLeapYear(year):
    return ((year % 4 == 0) and not(year % 100 == 0)) or (year % 400 == 0)

def getDaysInMonth(month, year):
    if month == 2:
        daysInMonth = 29 if isLeapYear(year) else 28
    elif month in (4, 6, 9, 11):
        daysInMonth = 30
    else:
        daysInMonth = 31
    return daysInMonth

def isValidDate(day, month, year):
    return day >= 1 and day <= getDaysInMonth(month, year) and \
           month >= 1 and month <= 12 and \
           year >= 0 and year <= 2099

def getMonthName(month):
    if month == 1:
        monthName = "January" 
    elif month == 2: 
        monthName = "February" 
    elif month == 3: 
        monthName = "March" 
    elif month == 4: 
        monthName = "April" 
    elif month == 5: 
        monthName = "May" 
    elif month == 6: 
        monthName = "June" 
    elif month == 7: 
        monthName = "July" 
    elif month == 8: 
        monthName = "August" 
    elif month == 9: 
        monthName = "September" 
    elif month == 10: 
        monthName = "October" 
    elif month == 11: 
        monthName = "November" 
    elif month == 12: 
        monthName = "December" 
    else:
        monthName = "Not Known"     # Should never happen
    return monthName

def getDaySuffix(day):
    if day in (1, 21, 31):
        suffix = "st"
    elif day in (2, 22):
        suffix = "nd"
    elif day in (3, 23):
        suffix = "rd"
    else:
        suffix = "th"
    return suffix

def displayAllDatesInMonth(month, year, verbose=False):
    print("Dates in %s, %d" % (getMonthName(month), year))
    for day in range(1, getDaysInMonth(month, year)+1):
        if verbose:
            print("%d%s %s %d" % (day , getDaySuffix(day), getMonthName(month), year))
        else:
            print("%02d/%02d/%04d" % (day , month, year))

def displaySpecialDatesInMonth(month, year, *specialDays, verbose=False):
    print("Special dates in %s, %d" % (getMonthName(month), year))
    for day in specialDays:
        if verbose:
            print("%d%s %s %d" % (day , getDaySuffix(day), getMonthName(month), year))
        else:
            print("%02d/%02d/%04d" % (day , month, year))


# -----------------------------------------------------------------
# Client code
# -----------------------------------------------------------------

#Ask the user for a day, month, and year.
day   = int(input("Enter a day (1-31): "))
month = int(input("Enter a month (1-12): "))
year  = int(input("Enter a year (0 to 2099): "))

print("%02d/%02d/%04d valid? %s" % (day, month, year, isValidDate(day, month, year)))

# Display all dates in month (first verbose, then not verbose)
displayAllDatesInMonth(month, year, True)
displayAllDatesInMonth(month, year)

# Display special days in December for the current year (first verbose, then not verbose).
displaySpecialDatesInMonth(12, year,
                           3, 25, 26, 31,
                           verbose=True)

displaySpecialDatesInMonth(12, year, 3,
                           25, 26, 31)
