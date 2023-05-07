'''
#Program to find length of the password given by user

u_name = input("Enter the username : ")
u_psswd = input("Enter the user password : ")

print(f"Hi {u_name}. Your password "+"*"*len(u_psswd) +" is "+ str(len(u_psswd)) +" characters long")
#str is used before len function as it returns integer which we need to convert to string before concatenation
#Efficient way to write this is as follows
print(f"Hi {u_name}. Your password is {len(u_psswd)} characters long" )


'''
#Now coming to readibility of code. Notice the above code is a bit complicated to read. To make it more simple where each line adds something simple to the code :

u_name = input("Enter the username : ")
u_psswd = input("Enetr the user password : ")
psswd_length = len(u_psswd)
hidden_psswd = "*"*psswd_length
print(f"Hi {u_name}. Your password {hidden_psswd} is {psswd_length} characters long")
#In formatted string, try avoiding concatenation, rather assign a different variable to avoid adding strings
print(u_psswd[::-1]) #To reverse the password