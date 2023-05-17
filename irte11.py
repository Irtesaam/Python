# Tuples
# they are like list but are immutable
# [list] , {dict} , (tuple)

my_tuple = (1,2,3,4,5,5,5,6,2,3,9)
print(my_tuple)
# my_tuple[1]='x' This wouldnt work as the tuple is immutable
print(my_tuple[2]) # we can access it by index
print(4 in my_tuple)
print(5 in my_tuple)
print(my_tuple.count(5)) # counts how many times 5 appears in the tuple
print(my_tuple.index(5)) # tells 1st index of the element
print(len(my_tuple)) # tells length of the tuple