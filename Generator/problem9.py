# Q9. Generator to yield characters of a string one by one.

def string_gen(text):
    for ch in text:
        yield ch

for c in string_gen("Hello"):
    print(c)


#  Logic:

# Loop har character ko yield karta hai.
# Ek-ek char print hota hai.
#  Real-Life Example:
# Typing animation effect ya encryption character-by-character me use hota hai.