# enumerate function in for loop 

for i in enumerate('Hellloooo'): # enumerate gives the index and the character of that index
    print(i)
    
for i, char in enumerate('Helllooo'): # This will print without tuple data type
    print(i,char)
    
    
# enumerate index of 50 in list :

for i,char in enumerate(list(range(1,101))):
    if char==50:
        print(f'The index of 50 is : {i}')