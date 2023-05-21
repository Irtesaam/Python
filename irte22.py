# Functions
# Functions are helpful for the DRY reason as it allows us to call a function which we defined witout writing it all over

pic = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
image = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]


def show_pic(): # defined a function to use it over and over without writing everything again
    for i in pic:
        for j in i:
            if j == 1:
                print("*", end='')
            else:
                print(' ', end='')
        print('')
    for row in image:  
        for column in row:
            if (column == 1):
                print('*', end='')
            else:
                print(' ', end='')
        print('')

show_pic() # calling function
show_pic() 
print(show_pic) # Prints memory alloted to this function
