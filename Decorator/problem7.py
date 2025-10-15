
# 7. Write a decorator that checks if all arguments to the function are integers; 
# if not, raise a ValueError.

# ye decorator input validation ke liye hai —
# matlab function ke arguments check karega ki sab integers hain ya nahi,
# aur agar koi argument integer nahi hua, to ValueError raise karega


def check_integers(func):
    def wrapper(*args, **kwargs):
        # Check all positional arguments
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError(f"All arguments must be integers! Found: {arg}")
        
        # Check all keyword arguments
        for key, value in kwargs.items():
            if not isinstance(value, int):
                raise ValueError(f"Argument '{key}' must be an integer! Found: {value}")
        
        # If all are integers, call the original function
        return func(*args, **kwargs)
    
    return wrapper


@check_integers
def add(a, b):
    return a + b


#  Correct call
print(add(5, 10))

# Incorrect call (will raise ValueError)
print(add(5, "vikas"))


# Example (sirf words me)

# Agar tum function ko add(5, 10) call karte ho →
# wrapper dekhega 5 aur 10 dono int hain → asli add chalega → result return.

# Agar tum add(5, "vikas") call karte ho →
# wrapper dekhega second argument string hai → 
# ValueError raise kar dega → asli add kabhi execute nahi hoga.