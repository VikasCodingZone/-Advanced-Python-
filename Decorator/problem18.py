# 18. Write a decorator that multiplies the return 
# value of the function by 2 (assuming numeric output).

# Ek decorator banana hai jo function ka output (return value) capture kare
# aur usse 2 se multiply karke return kare.

def multiply_by_2(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)   # Call original function
        return result * 2                # Multiply by 2 and return
    return wrapper
# Example usage
@multiply_by_2
def add(a, b):
    return a + b

@multiply_by_2
def square(n):
    return n * n

# Test calls
print(add(5, 3))     # (5+3) * 2 = 16
print(square(4))     # (4*4) * 2 = 32


# Logic (Step-by-Step)

# Decorator function original function ko input me leta hai.
# Wrapper function function call karta hai aur return value ko store karta hai.
# Wrapper function numeric return value ko 2 se multiply karta hai.
# Wrapper function modified value ko return karta hai.

# Real-Life Examples

# Pricing Calculations
# Function product price return karta hai → decorator se 
# double price calculate kar sakte ho (e.g., special offer).
# Score Multiplier in Games
# Function player score calculate karta hai → decorator score ko 2x kar de.
# Data Transformation Pipelines
# Function numeric data produce karta hai → decorator se values ko scale kar sakte ho.