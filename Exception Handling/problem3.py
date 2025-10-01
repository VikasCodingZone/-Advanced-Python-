# 3. ZeroDivisionError raised
try:
    result = 1 / 0
except Exception:
    print("Caught general exception")
except ZeroDivisionError:
    print("Caught division error")


#  Answer → b) "Caught general exception"
# Reason: ZeroDivisionError is a subclass of Exception,
#  aur except Exception पहले match ho gaya Python