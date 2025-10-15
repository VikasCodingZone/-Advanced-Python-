# 16. Implement a decorator that ensures the decorated function
#  is only called once (subsequent calls return None).

# Ek decorator banana hai jo ye ensure kare ki function sirf pehli baar chale.
# Baad me function call kiya jaaye → kuch execute na ho aur None return ho.


def call_once(func):
    called = False   # flag variable to track if function has run

    def wrapper(*args, **kwargs):
        nonlocal called
        if not called:            # first call
            called = True
            return func(*args, **kwargs)
        else:                     # subsequent calls
            print(f"{func.__name__} has already been called once.")
            return None

    return wrapper


# Example usage
@call_once
def initialize():
    print("Initialization done!")

# Test calls
initialize()  # Output: Initialization done!
initialize()  # Output: initialize has already been called once.
initialize()  # Output: initialize has already been called once.


# Logic (Step-by-Step)

# Jab decorator function ke upar lagta hai (@call_once),
# ek flag variable banaya jata hai, maan lo: called = False.
# Jab function call hota hai, wrapper check karta hai:
# Agar called == False → function ko call karo aur called = True set karo.
# Agar called == True → function execute nahi hoga, sirf None return hoga.
# Flag variable outer function me store hota hai →
# ye persistent rehta hai har call ke liye.
# Wrapper function function call ko control karta hai.


# Real-Life Examples

# Initialization Function
# Kisi app ka setup sirf ek baar hona chahiye.
# Example: Database connection, config load, API key setup.
# Singleton Pattern
# Object sirf ek baar create ho.
# Decorator ensure karta hai ki object initialization function multiple times na chale.
# One-Time Notification
# User ko ek baar hi welcome message dikhana.
# Subsequent visits me message repeat na ho.