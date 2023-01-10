def parlindome(s):
    if s == s[::-1]:
        return True
    else:
        return False
    
max_Values = 0
for i in range(0,1000):
    for j in range(0,1000):
        if parlindome(str(i*j)):
            if (i*j) > max_Values:
                max_Values = i*j
print(max_Values)