
# 4. Write a decorator that measures and prints the execution
#  time of the decorated function using the time module.

# ek decorator banana hai jo function ko run karne me kitna
#  time lagta hai wo measure karke print kare 

import time   # time module se hum current time nikalenge

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()            # function start hone se pehle time
        result = func(*args, **kwargs) # original function call
        end = time.time()              # function end hone ke baad time
        print(f"Execution time of {func.__name__}: {end - start:.4f} seconds")
        return result
    return wrapper

@measure_time
def slow_function():
    print("Processing...")
    time.sleep(2)   # 2 second ka delay (example ke liye)
    print("Done!")

# Call function
slow_function()


# measure_time decorator ek function (func) ko input me leta hai.
# start me hum function start hone ka time store karte hain.
# func() ko call karke actual function run karte hain.
# end me hum function end hone ka time store karte hain.
# Dono ke difference (end - start) se hume execution time milta hai.
# .4f ka matlab hai time ko 4 decimal places tak round kar dena.


# Execution flow:

# Timer start hota hai
# Function run hota hai (2 second delay)
# Timer stop hota hai
# Time difference print hota hai

#  Logic in Simple Words
# Ye decorator function ke chalne me kitna time laga, wo calculate karke print karta hai.
# Ye performance check karne ke liye useful hota hai
#  — jaise koi code slow chal raha ho, to uska time nikalne ke liye.