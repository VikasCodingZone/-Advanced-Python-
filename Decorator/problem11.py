
# 11. Design a decorator that accepts an argument
# (e.g., number of repeats) and calls the decorated function that many times.



def repeat(num_times):  # <-- yeh decorator ka argument lega
    def decorator(func):  # <-- yeh actual decorator hai
        def wrapper(*args, **kwargs):  # <-- yeh function ko control karega
            for i in range(num_times):  # <-- function ko num_times baar call karega
                print(f"Run {i+1}:")
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(num_times=3)  # <-- function 3 baar chalega
def say_hello():
    print("Hello, Vikas!")


say_hello()


#  Simple Logic Samjho

# Imagine karo tum ek helper bana rahe ho —
# jo function ko repeat karne ka kaam kare.
# Tum helper ko bolte ho — “3 baar chalana”
# Helper ke paas tumhara function aata hai (say_hello)
# Helper us function ko 3 baar call kar deta hai
# Yahi decorator ke andar ho raha hai —
# bas har kaam alag function layer me band hai.

# Real time example

# Aise samjho jaise ek gift ke 3 wrapping layers ho:
# Bahar ka cover = repeat()
# Uske andar box = decorator()
# Uske andar asli gift = wrapper()
# Aur sabse andar — tumhara original function 