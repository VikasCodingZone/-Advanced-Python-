# 4. Nested try-except

# aagr  inner try handle nahi kar paya → exception outer try tak propagate hota hai.

# Example:

try:
    try:
        int("abc")  # ValueError
    except ZeroDivisionError:
        print("Inner handled")
except ValueError:
    print("Outer handled")


#  Output:

# Outer handled