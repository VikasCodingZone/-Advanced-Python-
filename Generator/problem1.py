#  1 Write a Python program using a generator function that yields numbers 
# in reverse order starting from a given number n down to 1.


def countdown(n):
    while n > 0:
        yield n
        n -= 1

gen = countdown(5)

print(next(gen))  # 5
print(next(gen))  # 4
print(next(gen))  # 3


# Step-by-Step Working:

# Function countdown(n) call hone par 
# immediately execute nahi hota — ek generator object return karta hai.
# gen = countdown(5)

# Jab hum next(gen) call karte hain:
# Function start hota hai aur yield n tak run hota hai.
# n = 5 yield karta hai aur pause ho jata hai.
# Next call next(gen) firse wahi se start hota hai jahan pe last time rukha tha.
# n ab 4 hai → yield 4
# Teesri call me n ab 3 hai → yield 3
# Jab n 0 ho jata hai, generator stop ho jata hai (StopIteration error internally raise hoti hai).