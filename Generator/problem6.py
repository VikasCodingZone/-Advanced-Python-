# Q6. Generator to yield prime numbers up to N.

def prime_numbers(n):
    for num in range(2, n + 1):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num

for p in prime_numbers(20):
    print(p)


#  Logic:

# Number divisible na ho to wo prime hai.
# yield har prime ko return karta hai.
#  Real-Life Example:
# Cryptography (encryption algorithms like RSA) me primes use hote hain.