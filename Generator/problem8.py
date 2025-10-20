# Q8. Infinite generator (infinite counter).

def infinite_counter():
    num = 1
    while True:
        yield num
        num += 1

gen = infinite_counter()
for _ in range(5):
    print(next(gen))


#  Logic:

# Infinite loop + yield → har baar next number milta hai.
#  Real-Life Example:
# Invoice number generator ya queue token system me use hota hai.