

# 5 Execution order with try + except + else + finally jab exception aata hai

# Explanation (Hindi me):

# try → code run hota hai sirf tab tak jab tak error nahi aata. Jis line pe error aaya,
# uske baad ka code skip ho jata hai.
# except → agar error catch hua to ye block run hota hai.
# else → ye tabhi run hotta hai jab koi error na aaye. Error aaya to ❌ skip.
# finally → ye hamesha run hota hai, chahe error ho ya na ho.

# Execution Flow (jab error aata hai):
# try (partial) → except → finally


try:
    print("Start")
    x = 10 / 0   # error yaha aayega
    print("This will not run")
except ZeroDivisionError:
    print("Caught error")
else:
    print("No error")
finally:
    print("Finally block")
