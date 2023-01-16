from itertools import permutations 
input_list = [i for i in input().split()]
if len(input_list) > 10:
    input_list = input_list[:10]
all_values = []
perm = permutations(input_list) 
min_values = 99999999999999
answer = min_values
for i in list(perm): 
    perm_to_list = list(i)
    if perm_to_list[0] != '0':
        values = int(''.join(perm_to_list))
        if values < min_values:
            min_values = values
            answer = values
    
print(answer)
    

