import math
startH,startM,endH,endM = input().split()
startH,startM,endH,endM = int(startH),int(startM),int(endH),int(endM)
diffH = abs(startH - endH)
diffM = abs(startM - endM)
alldiff = (diffH * 60) + diffM
#print(math.ceil(alldiff/60))
print(alldiff)
result = 0

if alldiff > 15 and alldiff < 180:
    result = (math.ceil(alldiff/60)*10)
elif alldiff >= 180 and alldiff < 360:
    result += (math.ceil(abs(180-alldiff)/60)*20)
    result += (math.ceil(abs(180)/60)*10)
    print(result)
elif alldiff >= 180 and alldiff < 360:
    result += (math.ceil(abs(180-alldiff)/60)*20)
    result += (math.ceil(abs(180)/60)*10)
elif alldiff >= 360:
    result = 200
print(result)