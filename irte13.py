# Conditional logic
# In python, interpreter takes the indentation as the sign of whether the line belongs to a conditional logic or not. If its not indented, then it treats it like a new line and if not then it treats it as a part of that condition. In C, there are curly braces used under such conditions which tells the compiler the statement for the given conditions

# Truthy and Falsy
username = str(input('Enter your username'))
psswd = str(input('Enter your password'))
if username and psswd: # this basically checks whether the user has filled the detail or not and if it is empty then its falsy
    print('You can login now')
else:
    print('Fill the details first')

# Ternary operator
# shortcut for if else statement
is_friend = True
can_message = "You are allowed to message" if is_friend else "You are not allowed to message"
print(can_message)

# short circuitng in programming basically means to overlook the unnecessary statement if its already 100% sure whats gonna happen. This basically makes the machine efficient with long written codes
# like print (1<2<3>4<5) this will short circuit just after checking 3>4 and will return false without going further

# one should keep in mind the readibility and short circuiting of code. If short circuiting makes the code harder to read, then prefer readibility

# == checks for the equality of expression even if interpreter needs to convert data type also. For eg : print(True == 1) is true because 1 represents true and interpreter converts it as print(bool(True) == 1)
# is checks whether they have same memory locations or not