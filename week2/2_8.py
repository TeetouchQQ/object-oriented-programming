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
    start_day = start_day.split('-')
    end_day = end_day.split('-')
    
    start_year,start_month,start_day = int(start_day[2]),int(start_day[1]),int(start_day[0])
    end_year,end_month,end_day = int(end_day[2]),int(end_day[1]),int(end_day[0])
    
    start_count_day = day_of_year(start_day,start_month,start_year)
    end_count_day = day_of_year(end_day,end_month,end_year)

    year_gap = 0
    for year in range(start_year,end_year):
        year_gap += day_in_year(year)
        print(year)
    return ((year_gap-start_count_day) + end_count_day) +1

print(date_diff("1-1-2018", "1-1-2020"))
#print(date_diff("25-12-1999", "9-3-2000"))