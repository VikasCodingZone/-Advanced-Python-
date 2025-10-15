# 3. Implement a decorator that logs the arguments passed to the decorated function

# Decorator banao jo function ke input arguments ko print/
# log kare jab wo function call kiya jaayedef log_arguments(func):

def log_arguments(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments passed to {func.__name__}:")
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)
        return func(*args, **kwargs)
    return wrapper

@log_arguments
def greet(name, age):
    print(f"Hello {name}, you are {age} years old!")

# Function call
greet("Vikas", 21)


# func → ye original function hai jise decorate karna hai.
# *args → function ke sabhi positional arguments (jaise "Vikas", 21).
# **kwargs → function ke sabhi keyword arguments (jaise age=21, name="Vikas"
# agar hum named call karein).
# wrapper() function ke andar hum arguments log karte hain
#  (print karte hain), aur fir original function ko call karte hain.

# Jab hum greet() call karte hain, actually wrapper() run hota hai.
# Step by step ye hota hai:
# Arguments log hote hain (print hota hai).
# Original greet() function call hota hai.
# Output print hota hai.

#  Logic in Simple Words
#  Ye decorator har baar function call hone par uske arguments log (print) karta hai.
# Yaani, ye function monitoring / debugging ke liye use hota hai.
# Without changing the function code, hum automatically dekh sakte hain kya arguments pass hue.