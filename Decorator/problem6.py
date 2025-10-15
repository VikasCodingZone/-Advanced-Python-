# 6. Create a decorator that caches the results of a function
# (simple memoization) using a dictionary.


def cache(func):
    stored_results = {}   # dictionary to store previous results (cache)

    def wrapper(*args):
        if args in stored_results:             # agar result pehle se available hai
            print("Fetching from cache:", args)
            return stored_results[args]        # cache se return karo
        print("Calculating new result:", args)
        result = func(*args)                   # otherwise, function ko call karo
        stored_results[args] = result          # result ko cache me store karo
        return result
    return wrapper

@cache
def slow_square(n):
    print(f"Computing square of {n}...")
    return n * n

# Function calls
print(slow_square(5))
print(slow_square(10))
print(slow_square(5))  # Cached result



# Logic in Simple Words

# Ye decorator ek cache (ya memory) banata hai jisme function ke
#  previous results store hote hain.
# Agar same input dobara milta hai, to dobara calculate nahi karta, 
# balki pehle se stored result return kar deta hai.

# Is process ko Memoization kehte hain 

#  Real-life Example

# Agar tumhara function heavy computation karta hai
#  (e.g., factorial, Fibonacci, ML model prediction, etc.),
# to caching se time bachta hai kyunki bar-bar same input ke liye computation nahi hota.