# exercise!
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
]

fill = '*'
empty = ' '

# if 1 print *, 0 print ' '
for row in picture:
    for pixel in row:
        if (1 == pixel):
            print(fill, end = '')
        else:
            print(empty, end = '')
    print('')   # newline for each row