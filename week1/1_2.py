Sinput = input()
Lcnt = 0
Ucnt = 0
for i in Sinput:
    if i.isupper():
        Ucnt += 1
    elif i.islower():
        Lcnt += 1
        
print(Ucnt)
print(Lcnt)
    
