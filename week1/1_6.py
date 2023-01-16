number = 10

for row in range(number):
    space = (' ')*((number-row)+1)
    hashtag = ('#')*(row+1)
    print(space+hashtag)