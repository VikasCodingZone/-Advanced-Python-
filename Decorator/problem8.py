# 8. Implement a decorator that adds a delay
# (e.g., 1 second) before executing the decorated function.


import time  # time module for delay

def add_delay(func):
    def wrapper(*args, **kwargs):
        print(" Waiting for 1 second before executing the function...")
        time.sleep(1)  # delay for 1 second
        result = func(*args, **kwargs)  # call the original function
        return result
    return wrapper

@add_delay
def say_hello(name):
    print(f"Hello {name}, welcome!")

# Call the decorated function
say_hello("Vikas")



#  Execution Flow
# User calls say_hello("Vikas")
# Wrapper runs → prints “Waiting for 1 second...”
# Program waits for 1 second (time.sleep(1))
# Original say_hello("Vikas") executes → prints "Hello Vikas, welcome!"

# Scenario: API Request Rate Limiting
# Problem:

# Koi website ya API ek samay me limited requests allow karti hai (rate limit).
# Agar hum continuously requests bhejte rahe, to server block kar dega.
# Solution:
# Hum function ke har call ke beech me delay lagate hain.
# Isse hum rate limit ko respect karte hain aur server ko overload nahi karte.

# Logic in Real Life Terms
# API call → server limit ke according slow hota hai.
# Decorator automatically pause kar deta hai har call ke beech me.
# Hum manual delay lagane ki zarurat nahi — code clean rehta hai.
# Ye concept web scraping, API polling, automated tasks me bohot common hai.