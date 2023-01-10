Sinput = input()
L_cnt = 0
U_cnt = 0
for i in Sinput:
    if i.isupper():
        U_cnt += 1
    elif i.islower():
        L_cnt += 1
        
print(U_cnt)
print(L_cnt)
    
