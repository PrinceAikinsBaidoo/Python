def is_leap(year):
    leap = False
    
    # Write your logic here
    st = 1900
    lt = 10 ** 5 + 1
    for year in range(st,lt):
        if year % 400 == 0 and year % 4 == 0 :
            leap = True
        elif year % 4 == 0 :
                leap  = True
        else :
            pass
    
    print( leap)
    print(lt)

year = int(input("Enter a value: "))
is_leap(year)