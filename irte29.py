# Scope - what variable do I have access to

a = 1 # global scope

def parent():
    a=10
    def local():
        return a # local scope
    return local()

print(parent())
print(a) # This is still 1 and not 5 because a=5 is only limited to local scope

# The following order followed in the above program

# Scope rules :
# Start with local scope, if its not defined there, then moves to :
# Parent scope, still not there, then to :
# Global scope, still not there, then to :
# Built in python functions