number = 10

for row in range(number):
    for col in range(number):
        if row+col < number:
            print(' ',end = "")
        else:
            print('#',end = "")
    print('#')