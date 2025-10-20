# Q2. Factorial of a number (n!)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


# Logic:

# factorial(5) = 5 × factorial(4)
# → 5 × 4 × 3 × 2 × 1 = 120