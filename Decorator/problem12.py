# 12. Implement a decorator that handles exceptions in the decorated
# function and prints a custom error message.

# Ek decorator banana hai jo function ke andar hone wale error (exception) ko handle kare
# aur ek custom error message print kare — instead of crashing the program.

def handle_exceptions(func):   # <-- decorator define kar rahe hain
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)   # <-- yahan function chalega
        except Exception as e:             # <-- agar koi error aayi
            print(f"Error occurred: {e}")
            print("Please check your input or try again!")
    return wrapper


@handle_exceptions
def divide(a, b):
    return a / b


# Test calls:
print(divide(10, 2))  # Normal case
print(divide(10, 0))  # Error case (ZeroDivisionError)


#  Logic:

# Tumne ek decorator banaya jo function ko try-except ke andar wrap karta hai.
# Jab function normal chalta hai → result return hota hai.
# Agar function me koi galti (error) ho jaaye → program band nahi hota,
# balki decorator apni custom message print karta hai.
# Isse program smooth rehta hai aur user ko samajhne layak error milti hai.

#  Example (Real-life Samajho)

# Socho ek calculator app me divide karne wala button hai.
# Agar user 10 ÷ 0 kare — normally program crash karega.
# Lekin agar decorator laga hai,
# toh app politely bolega:
# “ Error occurred: division by zero
# Please check your input or try again!”
# Yani error handle ho gayi, aur program safely chalta rahta hai 