list_X = ['aaac','bbb','ccc']
c = 'c'

def count_char_in_string(x,c):
    answer = []
    for values in x:
        temp = 0
        for x in values:
            if x == c:
                temp +=1
        answer.append(temp)
    return answer

print(count_char_in_string(list_X,c))
        
        
        
    