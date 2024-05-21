day = int(input("Enter your day of birth: "))
month = int(input("Enter your month of birth: "))
year = int(input("Enter your year of birth: "))

months = {
    1: "January",
    2: "February", 
    3: "March", 
    4: "April", 
    5: "May",
    6: "June",
    7: "July",
    8: "August", 
    9: "September",
    10: "October",
    11: "November",
    12: "December"
    }

if month > 12 or month <=0 :
    print("Invalid month entered.")
    month = None
else:
    for key, value in months.items():
        if month == key:
            month = value

if year % 4 == 0:
    if month == 2:
        if day > 29 or day <= 0:
            print("Invalid day entered.")
            day =  None
else:
    if month == 2:
        if day > 29 or day <= 0:
            print("Invalid day entered.")  
            day = None          
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day > 31 or day <= 0:
            print("Invalid day entered.")
            day = None
    else:
        if day > 30 or day <= 0:
            print("Invalid day entered.")
            day = None

if day == 1 or day == 21:
    day = str(day) + "st"
elif day == 2 or day == 22:
    day = str(day) + "nd"
elif day == 3 or day == 23:
    day = str(day)+ "rd"
else:
    day = str(day) + "th"
print(day, month, year)