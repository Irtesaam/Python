# Global keyword
# It is used to access the global value rather than local value
# Scope is there to save memory and is very useful when program gets larger and larger 

total = 0

def count():
    # total=0 # This resets the total value to 0 everytime it runs
    global total # This tell the interpreter to use global total for this
    total += 1
    return total

count() # 0 to 1
count() # 1 to 2
count() # 2 to 3
count() # 3 to 4
print(count()) # 4 to 5

# This is a better code as it removes the dependency of global variable and we can just use it as parameter
total =0
def counts(total):
    total += 1
    return total

print(counts(counts(counts(counts(counts(total))))))
    