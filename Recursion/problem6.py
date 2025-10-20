# Q6. Power of a Number (xⁿ)

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

print(power(2, 5))

# logic

# 2^5 = 2 * 2^4
#      = 2 * 2 * 2^3
#      = 2 * 2 * 2 * 2^2
#      = 2 * 2 * 2 * 2 * 2^1
#      = 32

# Real Life:

# Jaise tum ek bulb ko har second me 2x zyada bright kar rahe ho —
# to har step pichle step pe depend karta hai (recursive growth).