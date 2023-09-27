def is_leap_year(year):
    return (year%100!=0 and year%4==0) or year%400==0
def days_in_month(month , year=1990):
    if month==2:
        return 28+int(is_leap_year(year))        
    elif (month<8 and month%2!=0) or (month>=8 and month%2==0):
        return 31
    else:
        return 30
def date_value(day ,month, year):
    value=0
    y=year-1
    # total days elapsed till the end of previous year
    value = y * 365 + y//4  - y//100 + y//400
    # add total days passed till previous month of this year
    m=1
    while m<month:
        #print(f'Adding {days_in_month(m,year)} for {m}/{year}')
        value+= days_in_month(m,year)
        m+=1
    #add days of this month
    value+=day
    return value
def date_to_week_day(date,month,year):
    ref_date = date_value(1,1,2006)
    input_date= date_value(date,month,year)
    diff= (input_date-ref_date) % 7
    return diff
def print_dates_in_week_day(start_date, days):
    print(start_date, '\t', (start_date + 7), '\t', (start_date + 14), '\t', (start_date + 21), end = '')
    if((start_date + 28) <= days):
        print('\t', (start_date + 28), end = '')
def print_calendar_vertically(month, year):
    week_days = ["Sun","Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    start_day_pos = date_to_week_day(1, month, year)
    days = days_in_month(month, year)
    for i in range(7):
        print(week_days[i], end='')
        print('\t', end = '')
        if(i < start_day_pos):
            print('\t', end = ' ')
            start_date_in_row = (7 - start_day_pos) + i + 1
        else:
            start_date_in_row = (i - start_day_pos) + 1
        print_dates_in_week_day(start_date_in_row, days)
        print("\n")
print_calendar_vertically(9,2023)