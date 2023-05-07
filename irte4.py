#Formatted strings

name = 'Dom Cobb'
age = 55
print("Hi "+ name + ". You are " + str(age) + " years old") #str is used to convert int to str data type here

#Now with formatted strings this becomes somewhat very easy to use

print(f"Hi {name}. You are {age} years old.") #where f denotes the formatted string
#This f works in python3. In python2, we have to accomplish the same task as follows

print("Hi {}. You are {} years old.".format(name, age))


#String indexes

selfish = '01234567'
          #01234567
print(selfish[0]) #Calls out for string at index 0
print(selfish[1]) #Calls out for string at index 1
print(selfish[2]) #Calls out for string at index 2
print(selfish) #Calls out for string from 0 to 7 as it is calling entire variable

# [start vale:stop vale:stepover value] This basically tells to look for the string in that range of index only. This concept is called string slicing
print(selfish[0:4])
print(selfish[0:8:2])
print(selfish[1:]) #from index 1 all the way to last
print(selfish[:4]) #from index 0 to index 4
print(selfish[::2])
print(selfish[-1]) #negative means the index starts from backwards
print(selfish[-3])
print(selfish[::-1]) #used to reverse a string as -1 tells to step value from backwards!!!!!!!!!!!!!!!
print(selfish[::-2])

#We cant reassign the values of a string as string is immutable and thus cant be changed. The only we to change a string is to completely replace its value by defining that string later in the program