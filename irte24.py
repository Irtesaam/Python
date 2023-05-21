# return

def sum(num1, num2):
    num1+num2
    
print(sum(4,7)) # This returned none because there is no return value if the function is called. Functions always has to return something

def sum(num1, num2):
    return num1+num2 # to return its value and exit the function

total = sum(23,18)
print(sum(17,total))