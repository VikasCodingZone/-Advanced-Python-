# 10. try-finally without except



try:
    print("Start")
    1 / 0   # Error
finally:
    print("Cleanup in finally")


#  Output:

# Start
# Cleanup in finally
# Traceback (most recent call last):
#   ...
# ZeroDivisionError: division by zero

#  Explanation

# try run hota hai, error aata hai

# finally hamesha run hota hai (cleanup ke liye)

# Error propagate karke program crash ho jata hai (kyunki except nahi hai)