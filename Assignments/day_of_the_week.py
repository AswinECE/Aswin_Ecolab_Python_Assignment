def weekday(day,month,year):

    yeardigit = year%100

    yearcode = (yeardigit+(yeardigit//4))%7

    monthcode = (0,3,3,6,1,4,6,2,5,0,3,5)

    centurycode = (18 - (year // 100)) % 7

    dateNumber = day

    total = yearcode+monthcode[month]+centurycode+day-1-leapyear(year)

    return total%7

def leapyear(year):

    if year%4==0 and (year%400==0 or year%100!=0):
        return 1
    return 0
             
day,month,year = (input("enter the day month and year :")).split()
wekday = weekday(int(day),int(month),int(year))

if (wekday == 0):
    print('Sunday')
elif (wekday == 1):
    print('Monday')
elif (wekday == 2):
    print('Tuesday')
elif (wekday == 3):
    print('Wednesday')
elif (wekday == 4):
    print('Thurdsday')
elif (wekday == 5):
    print('Friday')
elif (wekday == 6):
    print('Saturday')