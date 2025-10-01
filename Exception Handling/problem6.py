# 6. Raise inside except
try:
    1 / 0
except ZeroDivisionError:
    raise ValueError("New error")
finally:
    print("Finally")


#  Output:

# Finally
# Traceback (most recent call last):
#   ...
# ValueError: New error


# Reason: finally hamesha chalega cleanup ke liye, even if new error raised inside except.