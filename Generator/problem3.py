# Q3. Write a generator to yield Fibonacci sequence up to N terms.

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(7):
    print(num)


#  Logic:

# Har baar previous do numbers ka sum hota hai.
# yield sequence ka agla number return karta hai.

# Real-Life Example:
# Stock trend prediction ya population growth model me Fibonacci sequence ka use hota hai.