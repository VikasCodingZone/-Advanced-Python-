# Q10. Chain multiple generators (use yield from).

def gen1():
    yield from [1, 2, 3]

def gen2():
    yield from [4, 5, 6]

def combine():
    yield from gen1()
    yield from gen2()

for num in combine():
    print(num)


#  Logic:

# yield from ek generator ko doosre me merge karta hai.
# combine() dono generators ka data ek sequence me deta hai.
#  Real-Life Example:
# Multiple data sources (like user data + order data) combine karne me use hota hai.