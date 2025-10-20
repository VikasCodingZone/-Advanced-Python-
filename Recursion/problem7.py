# Q7. Sum of first N natural numbers

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(5))


# Logic:

# sum_n(5) = 5 + 4 + 3 + 2 + 1 = 15
# Stack me har call apna number rakhta hai, aur return hone par add karta hai.