# 9. Create a decorator that reverses the order of arguments
# passed to the decorated function.

# Ek decorator banaye jo jab function ko call karte ho,
#  uske positional arguments ka order reverse kar de.
# Example: agar function ko (1, 2, 3) pass hua → 
# decorator ke baad function ko (3, 2, 1) mile.

def reverse_args(func):
    def wrapper(*args, **kwargs):
        # Step 1: Positional arguments reverse karna
        reversed_args = args[::-1]
        print(f"Original args: {args}")
        print(f"Reversed args: {reversed_args}")
        
        # Step 2: Original function call with reversed arguments
        return func(*reversed_args, **kwargs)
    
    return wrapper

# Example function
@reverse_args
def display(a, b, c):
    print(f"a={a}, b={b}, c={c}")

# Call function
display(1, 2, 3)



# Step-by-Step Logic

# Decorator define karna

# reverse_args(func) ek decorator hai jo original function func ko input me leta hai.
#Ye ek wrapper function return karta hai.
# Wrapper function me arguments receive karna
# *args = positional arguments tuple me
# **kwargs = keyword arguments dictionary me
# Arguments ko reverse karna
# reversed_args = args[::-1] → ye ek naya tuple banata hai jisme 
# original arguments ulte order me hote hain.

# Original function call
# Original function ko reversed positional 
# arguments aur original keyword arguments pass kiye jaate hain:
# func(*reversed_args, **kwargs)

# Return value
# Original function ka output wrapper se return hota hai.
# Caller ko result bilkul normal function ke tarah milta hai.
# Print statements (optional)
# Debugging ke liye hum original aur reversed arguments print kar sakte hain.