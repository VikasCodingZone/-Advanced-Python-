
# 5. Design a decorator that converts the output of the decorated
# function to uppercase if it's a string.

def to_uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)     # original function call
        if isinstance(result, str):        # agar return value string hai
            return result.upper()          # usko uppercase me convert karo
        return result                      # warna jaisa hai waisa hi return karo
    return wrapper

@to_uppercase
def greet(name):
    return f"Hello {name}, welcome to Python programming language!"

# Calling decorated function
print(greet("vikas"))


# func → original function (jo decorator ke niche likha hai).
# wrapper() → ek inner function hai jo original function ko call karta hai.
# result → us function ka return value store karta hai.
# isinstance(result, str) → check karta hai ki return value string hai ya nahi.
# Agar string hai → usse .upper() karke uppercase me convert karta hai.
# Agar string nahi hai (jaise number ya list) → to usse as-it-is return karta hai.


# Step-by-step:

# greet("vikas") call hota hai → actually wrapper() run hota hai.
# Original greet() return karta hai → "Hello vikas, welcome to Python!"
# Decorator check karta hai — ye string hai 
# .upper() lagata hai → "HELLO VIKAS, WELCOME TO PYTHON!"
# Result print hota hai.

#  Logic in Simple Words
# Ye decorator function ke output ko check karta hai —
# agar wo string hai, to use uppercase me convert kar deta hai.
# Agar string nahi hai, to usse as-it-is return karta hai.