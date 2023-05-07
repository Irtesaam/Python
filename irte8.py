# Matrix 

# Matrix is a way to describe multidimensional lists. It has its practical use in machine learning and image processing

matrix = [ # This is an eg of 2D list as it contains list within list 
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[1][2]) # This is how we access the items in a multidimensional array

matrix2 = [ #These kind of notation can be used in image processing as it processes the image based on pixels on the screen
    [1,0,0],
    [0,1,0],
    [1,0,1]
]
print(matrix2[2][0]) # It access the 2nd index and then the 0th index and print the output