# sum of a list

my_list = list(range(1,101)) # shortcut to create list with elements 1 to 100
sum=0 # This must be defined outside loop becuase loop will reset the value to the initial for each time its iterated
for i in my_list:
    sum=sum+i # value of j is updated each time the loop is iterated
print('The sum of the items in the list is :',sum)
