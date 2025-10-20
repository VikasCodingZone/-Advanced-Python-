# Q3. Fibonacci Series

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

for i in range(6):
    print(fib(i), end=" ")

# Logic:

# Each term = sum of the previous two terms.
# Recursion tree:

# Real Life:

# Har next number pichle 2 number ke sum ke barabar hota hai
# (jese population growth ya rabbit pair problem).