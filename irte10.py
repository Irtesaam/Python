# Dictionary
# dict is unordered whereas list is ordered. A dict holds a lot more info than list

dictionary = {
    'a': [1, 2, 3], # a dict key has always to be immutable
    'b': 'hello', # In 90% cases, the key element has to be descriptive which mostly is by string
    'c': True,
    'age': 27
}
print(dictionary)
print(dictionary['a'])
print(dictionary['a'][0])
print(dictionary['b'])
print(dictionary['c'])
print(dictionary.get('rank')) # This is useful to check if the key element exist in the list or not without throwing any error as error terminates the program from running
print(dictionary.get('age', 55)) # This basically searches for age element in the dict and if doesnt exist then returns 55

my_list = [
    {
        'a': [1, 2, 3],
        'b': 'hello',
        'c': True
    },
    {
        'a': [4, 5, 6],
        'b': 'hello',
        'c': True
    }
]
print(my_list[1]['a'][2]) # accessing the element within list by indexing
list2 = my_list.copy() # creates a new list by copying the original list
print(my_list.clear()) # now if we clear the original list then list2 will still contain all the elements
print(list2)
print(list2.pop()) # randomly removes an item which is useful to randomly iterate a dict