list_x = [1,2,3]
list_y = [4,5,6]

def add2list(lst1,lst2):
    return [lst1_value + lst2_value for lst1_value,lst2_value in zip(lst1,lst2)]

print(add2list(list_x,list_y))