# For loops
# for <variable> in <collection> :
'''
for item in 'zzzzzzzzzzzzzzzzztttttttttttttttttttttttttttttmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmPQ':
    print(item) # in python, indententation tells the interpreter that the statement is in for loop
    print('hello')
print('hellooo')
print(item)
'''

'''
for item in (1,2,3,4,5,6,7,8):
    for x in ['a','b','c']:
        if x=='c':
            break
        print(item, x)
'''

# iterables : check one by one each item in that data type : dict, list, string, set, tuple. Integer is not iterable because it is not the collection of items 

user = {
    'name': 'Irte',
    'age': 19,
    'can_swim': False
}
for i in user.items() : # .items used to print the value of the variable along with varibles as tuple
    print(i)
for i in user.values() : # print only values
    print(i)
for i in user.keys() : # print only keys
    print(i)
for key, value in user.items() : # returns value not as tuple but separately
    print(key, value)