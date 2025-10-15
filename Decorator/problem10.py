# 10. Write a decorator that prints the name of the decorated function before it runs.

# Ek decorator banaye jo jab bhi function call ho
# Function ka name print kare
# Fir original function execute ho

def print_func_name(func):
    def wrapper(*args, **kwargs):
        print(f"Running function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Example function
@print_func_name
def greet(name):
    print(f"Hello {name}!")

# Call function
greet("Vikas")



#  Step-by-Step Logic 

# Decorator Function
# Ek decorator define karte hain jo original function (func) ko input me leta hai.
# Wrapper Function
# Decorator ke andar ek wrapper function define karte hain jo actual call handle karega.
# Wrapper me arguments (*args aur **kwargs) pass hote hain.
# Function Name Print Karna
# Wrapper ke start me func.__name__ se function ka name print karte hain.
# func.__name__ = Python attribute jo function ka naam string me deta hai.
# Original Function Call
# Wrapper ke andar original function ko call karte hain with *args aur **kwargs.
# Return Value
# Original function ka output wrapper se return hota hai.