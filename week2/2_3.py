input_list = [ [1, -3, 2], [-8, 5], [-1, -4, -3] ]



def delete_minus(x):
    return [[y for y in mini_list if y > 0]  for mini_list in x]

    
print(delete_minus(input_list))