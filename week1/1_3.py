import math
start_Hours,start_Minutes,end_Hours,end_Minutes = input().split()
start_Hours,start_Minutes,end_Hours,end_Minutes = int(start_Hours),int(start_Minutes),int(end_Hours),int(end_Minutes)
diff_Hours = abs(start_Hours - end_Hours)
diff_Minutes = abs(start_Minutes - end_Minutes)
all_difference = (diff_Hours * 60) + diff_Minutes

result = 0

if all_difference > 15 and all_difference < 180:
    result = (math.ceil(all_difference/60)*10)
elif all_difference >= 180 and all_difference < 360:
    result += (math.ceil(abs(180-all_difference)/60)*20)
    result += (math.ceil(abs(180)/60)*10)
elif all_difference >= 180 and all_difference < 360:
    result += (math.ceil(abs(180-all_difference)/60)*20)
    result += (math.ceil(abs(180)/60)*10)
elif all_difference >= 360:
    result = 200
print(result)