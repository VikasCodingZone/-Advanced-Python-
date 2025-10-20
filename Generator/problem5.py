# Q5. Generator to yield factorial of numbers up to N.

def factorial_gen(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        yield fact

for f in factorial_gen(5):
    print(f)

#  Logic:

# fact multiply hota jata hai har step me.
# Har baar yield se factorial milta hai.

#  Real-Life Example:
# Permutation-Combination (n!) me use hota hai — like password permutations.