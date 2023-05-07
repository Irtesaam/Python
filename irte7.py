#list
#List are similar to arrays which is used in different programming languages

cart = ['Books', 'Pen', 'Shirt', 'Pant', 'Laptop', 'Charger', 'Mobile phone', 'Earphone']
print(cart[1:6:2]) #List slicing is kinda similar to string slicing
print(cart)
'''
greet = 'hello'
greet[0] = 'f'
This wouldnt work as string is immutable but this can work with list as its mutable
'''
cart[1] = 'Geometry box' #This is possible because list is mutabke data type. Everytime we do list slicing, we are creating a copy of that list
new_cart = cart
neww_cart = cart[:] #This copies the list rather than changing the orginal list as it is using slicing
new_cart[0]='Notebooks' # This way the original list is modified as new_cart = cart
neww_cart[0]='Nothing'
print(cart[1:3]) #with list slicing we are creating a new list
print(new_cart)
print(neww_cart)
print(cart) # Still the cart will take the value of new_cart and not neww_cart because neww_cart used slicing which basically copies the list to make a new one which saves original from getting modeified

