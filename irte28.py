# Highest even

def highest_even(li):
    even = [] # necessary to append values from the li list which are even
    for item in li:
        if item%2==0:
            even.append(item)
    return max(even)
    # even.sort()
    # even.reverse()
    # return even[0] # This is also a valid solution but takes more lines, rather we just use predefined max function
        
print(highest_even([12,13,1,4,54,7,7,10,171,19]))