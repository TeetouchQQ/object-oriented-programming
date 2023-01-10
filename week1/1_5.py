def parlindome(s):
    if s == s[::-1]:
        return True
    else:
        return False
    
maxV = 0

for i in range(0,999):
    for j in range(0,999):
        if parlindome(str(i*j)):
            if (i*j) > maxV:
                maxV = i*j
print(maxV)