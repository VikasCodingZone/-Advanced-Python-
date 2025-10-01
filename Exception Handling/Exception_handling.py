# Python me program likhte waqt kabhi–kabhi error aa jata hai (jaise 0 se divide karna, file na milna, wrong input dena).
# Normally agar error aata hai to program crash ho jata hai.

# 👉 Exception Handling ka matlab hai:
# error ko pakadna aur program ko bina tode safely chalana.

# 🔑 Iske 4 part hote hain:

# try → yaha wo code likhte ho jisme error aane ka chance hai.
# except → agar error aata hai to ye block chalega.
# else → agar error nahi aata to ye chalega.
# finally → ye hamesha chalega, chahe error ho ya na ho (cleanup ke liye useful).

try:
    num = int(input("Ek number dalo: "))
    print("10 / number =", 10 / num)
except ZeroDivisionError:
    print("Bhai 0 se divide nahi kar sakte")
except ValueError:
    print(" Sirf number dalo, text nahi")
else:
    print(" Koi error nahi aaya")
finally:
    print(" Yeh line hamesha chalegi")


# 🔹 Real life example

# Socho tumne online payment kiya:
# try → Payment karne ki koshish.
# except → Agar balance kam hai / server down hai → error handle karke message dikhana.
# else → Agar payment sahi hua → “Payment Successful” message.
# finally → Bank ka system transaction close karega, chahe success ho ya fail.
# Simple shabdon me:
# Exception Handling ek tarika hai error ko pakadne ka, taki program bina rukke smoothly chale.

















