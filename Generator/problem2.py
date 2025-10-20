# Q2. Create a generator to yield even numbers up to N.

def even_numbers(n):
    for i in range(2, n + 1, 2):
        yield i

for e in even_numbers(10):
    print(e)


#  Logic:

# Loop 2 se start aur step 2 rakha gaya.
# yield har even number return karta hai.

#  Real-Life Example:
# Bus seat numbers (2,4,6,8,...) ke liye use ho sakta hai.