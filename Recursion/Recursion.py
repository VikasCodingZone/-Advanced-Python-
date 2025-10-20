# Recursion ek technique hoti hai jisme function khud ko hi call karta hai.
# Yani ek function apne andar se apne aap ko call karta hai — tab use recursion kehte hain.

# def greet():
#     print("Hello")
#     greet()  # function apne aap ko call kar raha hai

# greet()


# Base condition ek aisi condition hoti hai jo recursion ko stop karti hai.
# Agar base condition nahi doge, to program infinite chalta rahega aur error dega —
# RecursionError: maximum recursion depth exceeded.

def factorial(n):
    if n == 1:  # base condition
        return 1
    else:
        return n * factorial(n - 1)  # recursive call

print(factorial(5))

# Real-Life Example

# Socho tum ek mirror ke samne dusra mirror rakh do —
# tumhe apni image bar-bar repeat hoti dikhegi (infinite reflection).
# Wahi recursion jaisa hota hai — function apne aap ko call karta rehta hai,
# bas difference ye hai ki programming me hum base condition dekar rok dete hain.