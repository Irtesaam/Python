#Expression and statement

a=100
b=a/3 #here a/3 is an expression and b=a/3 is a statement
print(b)

#augmented assignment operator
value = 7
value += 4 # += meams variable = variable+4
print(value)

#strings in detail

print('Hello')
print("Hello")
print('''babu
  ...  kaise ho''') # ''' is used for long strings

#concatenation is adding two strings
print('Hello'+' World')

#Type conversion
a=str(100)
b=bool(a) #an int is converted into str and then to boolean type
print(type(b))

#Escape sequnce
weather = "It's \"kind of\" nice weather" #\ assumes the next input as str which helps us overcome the reserved keywords
print(weather)

#tab space
print("\t babu plz") #adds a tab space

#newline character
print("I am sorry babu \n"+"babu plzz") #breaks line