# while loops 

# infinite loop
'''
a=2
while a==2:
    print("Hello")
'''

# while loop

a=0
while a<100:
    print(a)
    a+=1 # represents a=a+1 and updates the value for each time the loop is iterated
else:
    print("The looping is over") #  Here else is useless as when the condition gets false, the else is executed but can also be printed by simple print function
    
a=0
while a<100:
    print(a)
    a+=1 
    break
else: # will be executed only when there is no break
    print("The looping is over") # Here else is useful as when the loop breaks, the else is not executed whereas if we had used print then it would have executed