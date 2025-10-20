# Q5. Reverse a string

def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("Vikas"))


# Logic:

# s[1:] → rest of string
# s[0] → first letter
# Recursion reverses the rest and then adds the first letter at the end.