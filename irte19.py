# for vs while loop

print('This is by for loop')
my_list = list(range(1,4))
for i in my_list:
    print(i)
    
print('This is by while loop')
i=0
while i<len(my_list):
    print(my_list[i])
    i+=1
    
# The general thumb rule is for loop is great for small iterations where we know how many times we have to loop but while loop is far better for larger iterations where range is not known or is quite large

while True:
    response = input('Say something : ')
    if response == 'bye': # This is most common use of while loop. i.e., when iterations is not fixed
        break

# break : break out of current running loop , continue : when it hits this, it again start the loop from beginning without jumping to next line , pass : its just passes to the next line (useful when we dont know what to write in a code in between but also want to run the program, then instead of using comment we can use pass statement)