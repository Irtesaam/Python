#Built in functions+Methods

quote = "you either die a hero or live long enough to become a villian"
print(quote.upper()) #convets the string to uppercase
print(quote.capitalize()) #capitalize the first letter of the sentence
print(quote.find("hero")) #finds whether the word exist in the variable or not and at which index
print(quote.replace("villian", "superhero")) #replaces the old part of string with new part
print(quote)


#simple program which guesses age from YOB

year = input("Enter the year you were born in : ")
age = 2023-int(year)
print(f"Your age is {age}")


#As a developer, commenting your code is very important. To understand best ways to comment, visit https://realpython.com/python-comments-guide/#python-commenting-best-practices
