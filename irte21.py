# check for duplicates in a list

my_list = ['a', 'b', 'g', 'g', 'c', 'a', 'd', 'g', 'a', 'f', 'z', 'z', 'y', 'e', 'd']
# iterate over each element
# sets can also be used

# My own code
duplicates = [] # necessary to store the duplicates in this variable
for i in my_list:
    j = my_list.count(i) # to count how many times an element occurs in a list
    if j > 1:
        duplicates.append(i) # add that value to duplicates variable. But this will repeat value in duplicates
        for k in duplicates:
            l = duplicates.count(k)
            if l>1:
                duplicates.remove(k) # This will remove the duplicates in the duplicates list and hence will only print elements which are repeated
duplicates.sort() # To make them in ascending order
print("The list of duplicates are : ",duplicates)

'''
Code in the solution. It is more efficient as it uses less resources and are of few lines only

duplicates = [] 
for i in my_list:
    j = my_list.count(i)
    if j > 1:
        if i not in duplicates:
            duplicates.append(i) 
duplicates.sort()
print("The list of duplicates are : ",duplicates)
 '''     