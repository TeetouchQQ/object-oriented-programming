def is_leap(Year):
  if (Year%4 == 0 and Year%100 != 0) or (Year%400 == 0) :   
    return True
  else:  
    return False
def day_in_year(Year):
  if(Year%4 == 0 and Year%100 != 0) or (Year%400 == 0) :   
    return 366
  else:  
    return 365

def day_of_year(day, month ,year):
    day_each_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    day_count = day + sum(day_each_month[:month-1])
    if is_leap(year) and month > 2:
        day_count += 1
    return day_count

def date_diff(start_day,end_day):
    day_each_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    start_date = start_day.split('-')
    end_date = end_day.split('-')
    
    start_year,start_month,start_day = int(start_date[2]),int(start_date[1]),int(start_date[0])
    end_year,end_month,end_day = int(end_date[2]),int(end_date[1]),int(end_date[0])
    
    if start_month > 12 or end_month > 12 or start_day > day_each_month[start_month] or end_day > day_each_month[end_month]:
        return -1
    elif is_leap(start_year) == False and start_month == 2 and start_day > 28:
        return -1
    elif is_leap(end_year) == False and end_month == 2 and end_month > 28:
        return -1
    elif start_year > end_year:
        return -1
    elif end_year == start_year and start_month > end_month:
        return -1
    elif end_year == start_year and end_month == start_month and start_day > end_day:
        return -1
    else:
        start_count_day = day_of_year(start_day,start_month,start_year)
        end_count_day = day_of_year(end_day,end_month,end_year)

        year_gap = 0
        for year in range(start_year,end_year):
            year_gap += day_in_year(year)
            #print(year)
        return ((year_gap-start_count_day) + end_count_day) +1

#print(date_diff("1-1-2018", "1-1-2020"))
#print(date_diff("25-12-1999", "9-3-2000"))
#print(date_diff("29-2-2020", "1-1-2020"))
#print(date_diff("29-2-2019", "1-4-2020"))