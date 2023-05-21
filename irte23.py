# Parameters and arguments

# Parameters is like a variable defined in function
def greet(name, age): # we can give default parameters here by name= and age= which will be printed if we just call greet()
    print(f"Hello {name}. You are {age} years old")

# Arguments is what we give as input
greet('Irte',18) # positional arguments
greet('Atfi',21)
greet(28, 'Rupert') # This will be wrong position matters
greet(age=23, name='Emma') # keyword arguments define explicitly which variables have given the value irrespective of position

# Always follow the order of parameters rather than assigning manually. This makes code review difficult for debugging purpose