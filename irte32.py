# Common errors
'''
1) TypeError : doing some operation between different data types that are not compatible. eg : print(1+'hello")
2) SyntaxError : not a valid python syntax. eg : def fun()
3) NameError : when we use a variable, function or module that is not defined yet
4) IndexError : accessing an index in a list that is out of range
5) KeyError : accessing a key that doesnt exist in a dict
6) ZeroDivisionError : eg : def division(num):
                                5/num
                            division(0) # This kind of input broke the program and give an error we didnt expected
'''

# Error handling

while True: # This is done to keep running the program until it gets right input
    try:
        age = int(input("Enter your age : "))
        print(age)
        print(10/age) # If we enter 0 as a input, it will still give error saying enter a number even though it is a number which makes it a buggy program. For such cases, we use except <typeoferror> we want to handle
    except ValueError: # This tells that if there is some excpetion in try block, then execute whatever is in except block which saves it from crashing
        print('Please enter a number')
    except ZeroDivisionError: # To handle zero division error
        print('Enter a number greater than 0')
    else: # This is to stop the program once it gets right input
        print('Thank you !')
        break
# We can use try..except..else block anywhere in our code to handle errors
    