# *args and **kwargs are the std name to give in the parameter for multiple enteries

def super_fun(*args, **kwargs): # By putting stars we can increase the nunber of arguments
    total = 0
    for items in kwargs.values(): # to pick value from kwargs
        total += items
    print(args) # arguments
    print(kwargs) # key word arguments
    return sum(args) + total
    
print(super_fun(1,2,3,3,7, num1 = 5, num2 = 19))

# Thumb rule : args , *args , defualt parameter , **kwargs