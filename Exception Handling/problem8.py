# 8. File doesn’t exist
try:
    open("nonexistent.txt")
except FileNotFoundError as e:
    print(f"Error: {e}")
else:
    print("File opened successfully")


#  Output:

# Error: [Errno 2] No such file or directory: 'nonexistent.txt'


# Reason: Error aaya → except चला, else skip ho gaya.