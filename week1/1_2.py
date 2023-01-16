Sinput = input()
Lower_cnt = 0
Upper_cnt = 0
for letter in Sinput:
    if letter.isupper():
        Upper_cnt += 1
    elif letter.islower():
        Lower_cnt += 1
print(Lower_cnt)    
print(Upper_cnt)
