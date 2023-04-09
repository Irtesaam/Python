#num = input("Enter a number : ") if data type is not defined, then it will assume it to be string
num = int(input("Enter a number : "))
for i in range(1,11): #upper limit-1 is till where range goes
    print(num, "*", i, "=", num*i)
    #comma is neccesary to separate strings and variables