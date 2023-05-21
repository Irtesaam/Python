# odd/even

def even_odd(num):
    if num%2==0:
        print(f"The number {num} is an even number")
    else:
        print(f"The number {num} is an odd number")
        
even_odd(2378561207)

# Below code is just to return boolean value for odd or even
def check_odd_even(num):
    return num%2==0

print(check_odd_even(12))
print(check_odd_even(11))