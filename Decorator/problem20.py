# 20. Implement a decorator that uses functools.
# wraps to preserve the original function's metadata.

# Question Logic

# Jab hum decorator banate hain, Python original function ka metadata
# (name, docstring, etc.) replace kar deta hai wrapper function se.
# functools.wraps use karne se:
# Original function ka __name__, __doc__, aur __module__ preserve hota hai
# Wrapper function original function ki tarah behave karta hai metadata-wise
# Use Case: Logging, debugging, documentation, APIs.

from functools import wraps

def preserve_metadata(func):
    @wraps(func)   # preserves original function metadata
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}'")
        return func(*args, **kwargs)
    return wrapper

# Example usage
@preserve_metadata
def greet(name):
    """This function greets a user by name."""
    print(f"Hello, {name}!")

# Test calls
greet("Vikas")
print("Function name:", greet.__name__)
print("Docstring:", greet.__doc__)
