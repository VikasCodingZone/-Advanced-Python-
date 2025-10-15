
# Decorator ek function ke upar ek cover jaisa kaam karta hai.
# Yani wo function ke pehle aur baad kuch extra kaam kar sakta hai bina uske original code ko badl

def my_decorator(func):
    def wrapper():
        print("Starting function")
        func()  # Original function call
        print("Ending function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, World!")

# Calling the decorated function
say_hello()



# Step-by-Step Explanation:

# Decorator Definition (my_decorator)

# def my_decorator(func):
#     def wrapper():
#         print("Starting function")
#         func()
#         print("Ending function")
#     return wrapper


# Yah ek decorator function hai jisme hum ek function (func) as argument le rahe hain.

# wrapper() ek inner function hai jo kuch extra kaam karta hai 
# (yaha print kar raha hai “Starting” & “Ending”) aur beech me original function ko call karta hai.

# @my_decorator Syntax

# @my_decorator
# def say_hello():
#     print("Hello, World!")


# Ye line ka matlab hai:

# say_hello = my_decorator(say_hello)


# Matlab say_hello() function ko my_decorator ke andar pass kiya gaya hai, 
# aur uska decorated version wapas assign hua hai.

# Function Call
# say_hello()


# Jab ye call hota hai, actually wrapper() function run hota hai.

# wrapper() pehle “Starting function” print karta hai,
# fir original say_hello() ko call karta hai,
# aur last me “Ending function” print karta hai.

#  Logic in Simple Words:

# Decorator ek function ke upar ek cover jaisa kaam karta hai.
# Yani wo function ke pehle aur baad kuch extra kaam kar sakta hai bina uske original code ko badle.

# Is example me:
# Function ke start me message print hua.
# Function ke end me message print hua.
# Ye sab decorator ne handle kiya — original say_hello() me koi change nahi hua.