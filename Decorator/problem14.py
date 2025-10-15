# 14. Write a decorator that counts and prints the number of times
#  the decorated function has been called (persistent count).

# Ek aisa decorator banana hai jo ye bataye ki function kitni baar call hua hai,
# aur har baar function chalne pe wo count print kare.
# Is count ko hum persistently (lagatar) badhate rahenge — reset nahi hoga.


def count_calls(func):
    count = 0  # <-- yahan hum call count store karenge

    def wrapper(*args, **kwargs):
        nonlocal count       # <-- outer variable use karne ke liye
        count += 1           # <-- har call pe 1 badh jaayega
        print(f"Function '{func.__name__}' called {count} times.")
        return func(*args, **kwargs)
    return wrapper


@count_calls
def greet(name):
    print(f"Hello, {name}!")


# Test calls
greet("Vikas")
greet("Riya")
greet("Aman")



# Basic Logic 

# Jab decorator function ke upar lagta hai (@count_calls),
# tab wo ek counter variable banata hai — maan lo count = 0.
# Jab bhi function call hota hai, decorator ke andar ek wrapper function run hota hai.
# Har baar wrapper chalta hai:
# Counter 1 se badh jata hai → count += 1
# Fir wo message print karta hai → "Function called X times"
# Aur fir original function ko call karta hai.
# Kyunki counter variable outer function me bana hai,
# wo memory me bana rehta hai aur har call ke saath update hota rehta hai.
# Isko hi hum bolte hain → persistent count.


#  Example Samjho 

# Socho tumhara ek function hai greet(name)
# jo kisi user ko hello bolta hai 
# Ab tum chahte ho ki ye track kare:
# “Ye function ab tak kitni baar chal chuka hai?”

#  Real-Life Example

# Socho tumhara ek website counter hai —
# jab bhi koi user page kholta hai, tum dekhte ho kitni baar page open hua.
# Jaise:
# Pehli baar user aaya → “Visited 1 times”
# Dusra user aaya → “Visited 2 times”
# Teesra user aaya → “Visited 3 times”
# Bilkul wahi kaam yeh decorator kar raha hai,
# bas yahan “page” ki jagah “function” hai 