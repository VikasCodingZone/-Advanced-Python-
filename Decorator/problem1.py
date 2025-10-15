# 1. Create a decorator that takes a function and returns a new function that executes the original function twice.

def run_twice(func):
    def wrapper():
        func()   # first execution
        func()   # second execution
    return wrapper

@run_twice
def greet():
    print("Hello, Python!")

# Calling decorated function
greet()


# Step-by-Step Explanation:

# Decorator Definition

# def run_twice(func):
#     def wrapper():
#         func()
#         func()
#     return wrapper

# run_twice ek decorator function hai jo ek function (func) ko input me leta hai.
# wrapper() ek inner function hai jo original function ko do baar call karta hai.
# run_twice() wrapper function ko return karta hai — ye hi decorated function ban jata hai.

# Decorator Use

# @run_twice
# def greet():
#     print("Hello, Python!")


# Ye likhne ka matlab hai:
# greet = run_twice(greet)
# Matlab: greet() ab original nahi raha, balki decorated version ban gaya hai jisme function do baar chalega.

# Function Call
# greet()

# Jab greet() call hota hai → wrapper() execute hota hai → usme func() (yani greet()) do baar call hota hai.
# Isliye output me "Hello, Python!" do baar print hota hai.