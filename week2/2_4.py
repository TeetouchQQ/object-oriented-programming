input_list = [int(i) for i in input().split()]
def count_minus(str):
    return len([x for x in str if x < 0])
print(count_minus(input_list))
    
