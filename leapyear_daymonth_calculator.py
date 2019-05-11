Month_Days = [31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year % 4 == 0 and (year % 100!= 0 or year %  400 == 0)

def num_days_month(year,month):
    if month <1 or month > 12:
        return 'Invalid Month, Please give values between 1-12'
    if is_leap(year) and month == 2:
        return 28
    return Month_Days[month-1]

#print(num_days_month(2019,5))
    

    
