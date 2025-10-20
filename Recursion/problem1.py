# Q1. Print numbers from 1 to N using recursion

def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)   # recursive call
    print(n)               # print after returning

print_numbers(5)

# Logic:

# Function print_numbers(5) → print_numbers(4) → ... → print_numbers(0)

# Jab base case milta hai, tab stack reverse me return hota hai
# → isiliye 1,2,3,4,5 print hota hai.