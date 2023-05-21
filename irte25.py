# Methods vs Functions
# Functions has () and methods has . like .append etc

# Docstrings

def result():
    '''
    Info: This function prints result 
    '''
    # The above is an eg of docstring. This basically shows when we point cursor to the function or calls it
    print("You are passed")

result()
help(result) # This will print the docstring for the function
print(result.__doc__) # This also does the same thing