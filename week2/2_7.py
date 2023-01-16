def is_leap(Year):
  if((Year % 400 == 0) or (Year % 100 != 0) and (Year % 4 == 0)):   
    return True
  else:  
    return False
def day_of_year(day, month ,year):
    day_each_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    day_count = day + sum(day_each_month[:month-1])
    if is_leap(year) and month > 2:
        day_count += 1
    return day_count
print(day_of_year(27,12,2003))