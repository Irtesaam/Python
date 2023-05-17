# sets
# unordered collections of unique objects
# sets doesnt have indexing and we need to access it by element

my_set = {1,2,2,3,4,4,4,4,5,6,9,10,13,17,17}
print(len(my_set))
print(my_set)
my_set.add(101) # gets added
my_set.add(3) # doesnt because 3 is already there
print(my_set)

my_list = [1,23,4,56,43,2,2,4,4,4,71]
set1 = set(my_list) # To convert list to set and print only unique value
print(my_list)
print(set1)

# venn diagrams and its operations through set methods

set2 = {1,2,3,4,5}
set3 = {4,5,6,7,8,9,10}
set4 = {1}
print(set2.difference(set3)) # set2 - set3
set2.difference_update(set3) # this not only tells the difference but update it with the value 
print(set2)
print(set3.difference(set2)) # set3 - set2
set2.discard(2) # discards element 5 from set2
print(set2)
print(set2.intersection(set4)) 
print(set2.union(set3)) # takes union of set

# rest all operations are similar to venn set operations in mathematics
# while coding refer to python documentation on w3schools to refer to anything
