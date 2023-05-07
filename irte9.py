# List method

#adding 

basket = [1,2,3,4,5]
basket.append(100)
print(basket) # append adds the new value to the end of the list
print(basket.append(100)) # This returns none because append changes list in place and doesnt produce anything in return as output as it doesnt produce any copy of the list. To print result, we need to print the list itself

# To insert values anywhere on the list , we use insert 

basket.insert(2, 3.5) # index and object
print(basket)

# To add multiple items , use extend

basket.extend([101,102,103,104]) # This basically extends the list
print(basket)


#removing
'''
basket = [1,2,3,4,5]
basket.append(100)
print(basket)
basket.pop() #pop basically removes the last item of the list which is 100 as we addes it before
print(basket)
basket.pop(1) # removes object at index 1
print(basket)
basket.remove(3) # This removes the value given itself 
print(basket)
basket.clear() # clears entire list
print(basket)
'''

# indexing
'''   # windows+v will list all things you copied 
basket = ['a','b','c','d','e','f','d']
print(basket.index('d')) # finds the index of object d
print('d' in basket) # checks whether the object is present in the list or not
print('z' in basket)
print(basket.count('d')) # counts how many times an object appeared in list
'''

#sorting
'''
basket = ['a','b','c','x','y','d','e','f','d']
print(sorted(basket)) # This doesnt modify the original list rather just copies the original and then changes it
print(basket)
basket.sort() # sorts the list in order and thus modifies the original list
print(basket)
print(basket) # This original list is modified as we used sort function
basket.reverse() # reverses the list that swicthing the indexes without sorting if not sorted first
print(basket)
print(basket[::-1]) # modifies the list
'''

#ranges
'''
print(list(range(1,100))) # This will print a list from 1 to 99 as the last value to stop before is 100
print(list(range(101))) # This will print the list form 0 to 100 which contains 101 items

new_sentence = '!'.join(['Hi','My','name','is','Irte']) # join basically combines the list to the string as is very commonly used
print(new_sentence)
'''

#list unpacking
'''
a,b,c, *other, d= [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(a)
print(b)
print(c)
print(other)
print(d)
'''