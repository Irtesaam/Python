# simple GUI to show how does binary works

pic = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for i in pic:
    for j in i:
        if j == 1:  # == is necessary to check the equality of j index
            # print() is by default a new line that is print(end='\n') which we changed here as we dont want a new line right here
            print("*", end='')
        else:
            print(' ', end='')
    print('')  # The problem now was that there were no new lines created, so for a new line after each iterations, we need to add empty string after each iteration as that by default is a new line or we can write print(end='\n')

image = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for row in image:  # here variables names are chosen in right ways as its self explanatory unlike last one. Naming variables in better way can increase the readibility of that code
    for column in row:
        if (column == 1):
            print('*', end='')
        else:
            print(' ', end='')
    print('')

# writing cleaner code :

img = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

fill = '*' # using these extra lines of code is better because if we are using print multiple times and now we want to change fill variable, then we will have to change in each if we didnt created this variable
empty = ' '
for row in img:  # here variables names are chosen in right ways as its self explanatory unlike last one. Naming variables in better way can increase the readibility of that code
    for column in row:
        if (column): # not necessary to write ==1 because by default it will look for true value
            print(fill, end='')
        else:
            print(empty, end='')
    print('')
