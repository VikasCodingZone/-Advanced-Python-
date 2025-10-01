# 9. Multiple except blocks

# Python top-to-bottom check karta hai → jo pehle match hota hai wahi run hoga.



try:
    1 / 0
except Exception:
    print("General")
except ZeroDivisionError:
    print("Specific")


# Output:

# General


#  Order important hai → hamesha specific exceptions pehle likho, phir general.