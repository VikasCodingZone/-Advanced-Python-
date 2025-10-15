
# 17. Create a decorator that logs the return value of the decorated function.

# Ek decorator banana hai jo function ka output (return value) capture kare
# aur usse log ya print kare.


def log_return(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)   # Call the original function
        print(f"Function '{func.__name__}' returned: {result}")  # Log return value
        return result                   # Return value unchanged
    return wrapper
# Example usage
@log_return
def add(a, b):
    return a + b

@log_return
def greet(name):
    return f"Hello, {name}!"

# Test calls
add(5, 3)        # Function 'add' returned: 8
greet("Vikas")   # Function 'greet' returned: Hello, Vikas!


# Logic (Step-by-Step)

# Decorator function original function ko input me leta hai.
# Wrapper function function call karta hai aur return value ko store karta hai.
# Wrapper function return value ko print/log karta hai.
# Wrapper function return value ko original call me return bhi karta hai,
# taaki original behavior maintain ho.



# Real-Life Examples

# Debugging
# Functions ke outputs check karne ke liye, bugs trace karne ke liye.
# API Monitoring:
# Web API ke responses log karne ke liye.
# Analytics:
# User action ke return values ko track karne ke liye (jaise scores, calculations).