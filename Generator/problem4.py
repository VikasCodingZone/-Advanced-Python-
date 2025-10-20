# Q4. Generator to yield squares of numbers.

def squares(n):
    for i in range(1, n + 1):
        yield i ** 2

for sq in squares(5):
    print(sq)


#  Logic:

# i**2 se har number ka square milta hai.

#  Real-Life Example:
# Area calculations (side²) ke liye — like square plots ka area nikalna.