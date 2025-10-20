# Q4. Sum of digits of a number

def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(1234))


# Logic:

# 1234 → 4 + 3 + 2 + 1 = 10
# Break hota hai by %10 (last digit) aur //10 (remove last digit).