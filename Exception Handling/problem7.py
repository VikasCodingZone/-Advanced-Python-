# 7. Can else run without except?

# No → else ke liye कम से कम ek except होना जरूरी है.

# Yes → finally अकेले try ke saath valid hai.

# Explanation (Hindi me):

# No → else block tabhi valid hai jab kam se kam ek except block ho
# . Agar except nahi hai to else likhne pe Python syntax error dega.

# Yes → finally block alag case hai.
#  finally ko aap try ke saath akela bhi use kar sakte ho, bina except ke.



# Example 1 ( Invalid — else without except):
# try:
#     print("Hello")
# else:
#     print("No error")   # SyntaxError aayega


# Example 2 ( Valid — try with finally only):
try:
    print("Hello")
finally:
    print("Always run")